import logging

def setup_logger(name="botlog"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

logger = setup_logger()
    