import logging
import os
import sys
from pathlib import Path

import yaml


def get_config() -> dict:
    """ Loads config from YML file and sets up logging """
    try:
        project_root = Path(__file__).parent.parent.parent
        config_path = os.path.join(project_root, 'config', 'config.yml')

        with open(config_path, 'r') as yml_file:
            config = yaml.safe_load(yml_file)

        log_file_path = os.path.join(project_root, 'logs',
                                     config['logging']['log_file_name'])
        date_strftime_format = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(filename=log_file_path,
                            filemode='a',
                            datefmt=date_strftime_format,
                            format='[%(levelname)s] %(asctime)s: %(message)s',
                            level=logging.DEBUG)

        # Also print logging messages to print to stdout
        # Source: https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
        # Source: https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

        logging.info('Configuration loaded')
        return config

    except Exception as err:
        logging.error(f'Configuration failed to load {err}')
