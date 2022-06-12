import config_loader

if __name__ == '__main__':
    config = config_loader.get_config()

    print(config["logging"])
    print(config["scraping"])
