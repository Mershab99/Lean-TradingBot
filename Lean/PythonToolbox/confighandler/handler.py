from dotenv import load_dotenv
import logging
import sys


class LogHandler:
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    @classmethod
    def get_logger(cls):
        return cls.root


class ConfigHandler:
    def __init__(self, path):
        load_dotenv(dotenv_path=path)
