"""
The `logger` module provides a Logger class for convenient logging.

Classes:
    Logger: Represents a logger for logging messages.
"""
import logging


class Logger:
    """
    The `logger` module provides a Logger class for convenient logging.

    Classes:
        Logger: Represents a logger for logging messages.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Logger class.
        """
        self.logger = logging.getLogger(self.__class__.__name__)

    def log_error(self, message: str) -> None:
        """
        Logs an error message.

        This method logs an error message using the logger instance.

        Args:
            message (str): The error message to log.

        Returns:
            None
        """
        self.logger.error(message)

    def log_warning(self, message: str) -> None:
        """
        Logs a warning message.

        This function logs a warning message using the logger instance associated with the class.

        Parameters:
            message (str): The warning message to be logged.

        Returns:
            None
        """
        self.logger.warning(message)

    def log_info(self, message: str) -> None:
        """
        Logs an informational message.

        This function logs an informational message using the logger instance associated with the class.

        Parameters:
            message (str): The informational message to be logged.

        Returns:
            None
        """
        self.logger.info(message)

    def log_debug(self, message: str) -> None:
        """
        Logs a debug message.

        This function logs a debug message using the logger instance associated with the class.

        Parameters:
            message (str): The debug message to be logged.

        Returns:
            None
        """
        self.logger.debug(message)
