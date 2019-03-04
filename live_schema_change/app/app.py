import logging
import random
import time

import click
import numpy as np
from config import config
from db import metadata1, metadata2, view_1, click_1, click2_1, view_2, click_2, click2_2
from fsa import FSA
from sqlalchemy import create_engine, select, insert

log = logging.getLogger("app")


@click.command()
@click.option("--version")
def setup_database(version):
    version = int(version)
    engine = create_engine(config["db_connect"])
    if version == 1:
        metadata1.create_all(engine)
    else:
        metadata2.create_all(engine)


def insert_v1(result, connection):
    """Insert the version 1 FSA result into the db"""
    log.debug(f"result {result}")
    if result is None:
        return
    if result['event_type'] == 'view':
        connection.execute(view_1.insert().values(id=result['id'],
                                                  timestamp=time.monotonic()))
    elif result['event_type'] == 'click':
        connection.execute(click_1.insert().values(id=result['id'],
                                                   timestamp=time.monotonic()))
    elif result['event_type'] == 'click2':
        connection.execute(click2_1.insert().values(id=result['id'],
                                                    timestamp=time.monotonic()))
    else:
        log.error(f"Received unrecognized event_type in result {result}")


def insert_v2(result, connection):
    """Insert the version 1 FSA result into the db"""
    log.debug(f"result {result}")
    if result is None:
        return
    if result['event_type'] == 'view':
        connection.execute(view_2.insert().values(id=result['id'],
                                                  type=result['fsa_type'],
                                                  timestamp=time.monotonic()))
    elif result['event_type'] == 'click':
        connection.execute(click_2.insert().values(id=result['id'],
                                                   type=result['fsa_type'],
                                                   timestamp=time.monotonic()))
    elif result['event_type'] == 'click2':
        connection.execute(click2_2.insert().values(id=result['id'],
                                                    type=result['fsa_type'],
                                                    timestamp=time.monotonic()))
    else:
        log.error(f"Received unrecognized event_type in result {result}")


@click.command()
@click.option("--version")
def generate_transactions(version):
    fsas = []
    insert_fn = insert_v1 if int(version) == 1 else insert_v2
    engine = create_engine(config["db_connect"])
    conn = engine.connect()
    for idx in range(config['fsa1_count']):
        fsas.append(FSA(idx, lambda x: insert_fn(x, conn), 1, config['fsa1']))
    for idx in range(config['fsa2_count']):
        fsas.append(FSA(config['fsa1_count'] + idx, lambda x: insert_fn(x, conn), 1, config['fsa2']))
    idx = config['fsa1_count'] + config['fsa2_count']
    while len(fsas) > 0:
        fsa = random.choice(fsas)
        fsa.step()
        if fsa.done():
            log.debug(f"FSA({fsa.fsa_id}) done")
            fsas.remove(fsa)
        if random.uniform(0, 1) < config['fsa1_birthrate']:
            log.debug("new fsa1")
            fsas.append(FSA(idx, lambda x: insert_fn(x, conn), 1, config['fsa1']))
            idx += 1
        if random.uniform(0, 1) < config['fsa2_birthrate']:
            log.debug("new fsa2")
            fsas.append(FSA(idx, lambda x: insert_fn(x, conn), 2, config['fsa2']))
            idx += 1
        log.debug(f"counts {np.unique([f.fsa_type for f in fsas], return_counts=True)}")


@click.command(name="monitor")
@click.option("--version")
def monitor_transactions(version):
    version = int(version)
    cutoff = time.monotonic() - config['monitor_interval_seconds']
    engine = create_engine(config["db_connect"])
    conn = engine.connect()
    if version == 1:
        log.info("perform analysis without types")
        while True:
            views = conn.execute(select([view_1]).where(view_1.c.timestamp > cutoff)).fetchall()
            clicks = conn.execute(select([click_1]).where(click_1.c.timestamp > cutoff)).fetchall()
            click2s = conn.execute(select([click2_1]).where(click2_1.c.timestamp > cutoff)).fetchall()
            log.info(click2s)
            time.sleep(1)
    else:
        log.info("perform analysis with types")
        while True:
            views = conn.execute(select([view_2]).where(view_2.c.timestamp > cutoff)).fetchall()
            clicks = conn.execute(select([click_2]).where(click_2.c.timestamp > cutoff)).fetchall()
            click2s = conn.execute(select([click2_2]).where(click2_2.c.timestamp > cutoff)).fetchall()
            log.info(click2s)
            time.sleep(1)


@click.group()
def main():
    log.info("Running")


main.add_command(setup_database, name="setup")
main.add_command(generate_transactions, name="generate")
main.add_command(monitor_transactions, name="monitor")

if __name__ == '__main__':
    main()
