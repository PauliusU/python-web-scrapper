import yaml

config_path = "../../config/config.yml"


def get_config() -> dict:
    """ Loads config from YML file """
    with open(config_path, "r") as yml_file:
        return yaml.safe_load(yml_file)
