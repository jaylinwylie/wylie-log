import logging
from functools import wraps

logging.getLogger().setLevel(logging.DEBUG)


def draw_layers(count: int) -> str:
    """Generates a `⎢` string to represent the depth of the current call."""
    return "⎢" * count


class WylieLog:
    """
    logging utility class with support for dynamic call depth tracking
    and function/class IO logging.
    """
    def __init__(self):
        self.layers = 0

        class LayeredFormatter(logging.Formatter):
            def format(self, record):
                if hasattr(record, "layers"):
                    record.msg = f"{draw_layers(record.layers)}{record.msg}"
                return super().format(record)

        handler = logging.StreamHandler()
        formatter = LayeredFormatter("%(message)s")
        handler.setFormatter(formatter)
        logging.getLogger().handlers.clear()
        logging.getLogger().addHandler(handler)

    def log_callable(self, func):
        """Decorator to log the inputs, outputs, and call depth of a function."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            module = func.__module__

            inputs = f"args={args}, kwargs={kwargs}"
            self._log_debug(f"⎡{module}.{func.__name__}({inputs})")
            try:
                self.layers += 1
                result = func(*args, **kwargs)
                self.layers -= 1
                self._log_debug(f"⎣{module}.{func.__name__} -> {result}")
                return result
            except Exception as e:
                self.layers -= 1
                self._log_error(f"Error in {module}.{func.__name__}: {e}")
                raise e

        return wrapper

    def log_class(self, cls):
        """Decorator to log all callable methods of a class."""
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                setattr(cls, attr_name, self.log_callable(attr_value))
        return cls

    def _log_debug(self, message):
        """Logs a debug message, injecting the current layer depth."""
        logging.getLogger().debug(message, extra={"layers": self.layers})

    def _log_error(self, message):
        """Logs an error message, injecting the current layer depth."""
        logging.getLogger().error(message, extra={"layers": self.layers})


logger_instance = WylieLog()


class LayeredLogAdapter(logging.LoggerAdapter):
    def __init__(self, logger, layered_logger):
        super().__init__(logger, {})
        self.layered_logger = layered_logger

    def process(self, msg, kwargs):
        kwargs["extra"] = kwargs.get("extra", {})
        kwargs["extra"]["layers"] = self.layered_logger.layers
        return msg, kwargs


log = LayeredLogAdapter(logging.getLogger(), logger_instance)
log_callable = logger_instance.log_callable
log_class = logger_instance.log_class
