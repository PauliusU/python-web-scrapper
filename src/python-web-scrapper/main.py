import config_loader
import scraper

if __name__ == '__main__':
    config = config_loader.get_config()
    scraper.scrape_site(config)
