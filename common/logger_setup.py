import logging


def configure_logger(log_file="default.log"):
    logger = logging.getLogger(__name__)
    if log_file.endswith(".log"):
        filename = log_file
    else:
        filename = log_file + ".log"

    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    return logger
