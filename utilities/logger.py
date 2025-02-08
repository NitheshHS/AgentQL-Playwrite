import logging

class Logger:
    def __init__(self, log_name="app_log", log_level=logging.DEBUG, log_file="../logs/app.log"):
        """
        Initializes the Logger with the provided settings.

        :param log_name: The name of the logger.
        :param log_level: The level of logging (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
        :param log_file: The path to the log file (if you want to log to a file).
        """
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)

        # Create a formatter to specify the log message format
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_format)

        # Create a console handler and set the formatter
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Create a file handler and set the formatter
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        """
        Logs a DEBUG message.
        """
        self.logger.debug(message)

    def info(self, message):
        """
        Logs an INFO message.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Logs a WARNING message.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Logs an ERROR message.
        """
        self.logger.error(message)

    def critical(self, message):
        """
        Logs a CRITICAL message.
        """
        self.logger.critical(message)
