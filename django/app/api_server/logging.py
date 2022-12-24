import logging


class AddLogLevel(logging.Filter):
    def filter(self, record):
        record.level = record.levelname
        record.logger = record.name
        return True
