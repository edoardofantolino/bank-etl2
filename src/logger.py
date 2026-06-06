import logging

def get_logger():
    logger = logging.getLogger("etl")
    logger.setLevel(logging.INFO)
    

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        # Console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File
        file_handler = logging.FileHandler("../logs/etl.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger