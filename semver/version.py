import click
from semver import parse, format_version
import logging
import sys

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger("version")
log.addHandler(handler)
log.setLevel(logging.INFO)


@click.command()
@click.option('--add-tag/--no-add-tag', default=False)
@click.option('--remove-tag/--no-remove-tag', default=False)
@click.option('--increment-version', default=None)
@click.option('--file')
def version(add_tag, remove_tag, increment_version, file):
    log.info(f"Version add_tag:{add_tag} remove_tag:{remove_tag} increment_version{increment_version} file {file}")
    assert not (add_tag and remove_tag)

    with open(file) as f:
        version_data = parse(f.read().strip())
    log.info(f"Read version_data: {version_data}")

    if increment_version:
        if increment_version == "MAJOR":
            log.info("incremented major")
            version_data["major"] += 1
        elif increment_version == "MINOR":
            log.info("incremented minor")
            version_data['minor'] += 1
        else:
            log.info("incremented patch")
            version_data['patch'] += 1

    if add_tag:
        assert version_data["prerelease"] is None
        log.info("set prerelease to stable")
        version_data["prerelease"] = "stable"

    if remove_tag:
        assert version_data["prerelease"] == "stable"
        log.info("remove prerelease info")
        version_data["prerelease"] = None

    with open(file, "w") as f:
        log.info(f"Written version data {version_data}")
        f.write(format_version(**version_data))


if __name__ == '__main__':
    version()
