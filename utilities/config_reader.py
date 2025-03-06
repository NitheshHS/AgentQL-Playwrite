import configparser
from distutils.command.config import config
from pathlib import Path

from utilities.logger import Logger


class ConfigReader:
    def __init__(self):
        # self.logger = Logger(log_name=self.__class__.__name__)
        self.config=configparser.ConfigParser()
        self.config.read(Path(__file__).parent.parent/'TestData'/'settings.ini')

    def get(self, section, option, default=None):
        # self.logger.info(f'reading {section}: {option}')
        if not self.config.has_section(section):
            return configparser.NoSectionError(section)
        return self.config.get(section, option, fallback=default)

