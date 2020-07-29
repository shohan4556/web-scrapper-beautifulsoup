import logging


def set_custom_loggin(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)

def report(e: Exception):
    logging.exception(str(e))