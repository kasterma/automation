import yaml
from logging.config import dictConfig


with open("logging.yaml") as log_conf_file:
    log_conf = yaml.load(log_conf_file)
    dictConfig(log_conf)

with open('config.yaml') as f:
    config = yaml.load(f)
