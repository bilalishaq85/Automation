import logging.config
from os import path


def singleton(myClass):
    instances = {}

    def get_instance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]

    return get_instance()


@singleton
class Logger:
    def __init__(self):
        log_file_path = path.join(path.dirname(path.abspath(__file__)), '../Utilities/log.conf')
        logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
        self.logr = logging.getLogger('AutomationAgent')
