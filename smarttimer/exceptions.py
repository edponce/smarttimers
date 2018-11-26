"""Exceptions for timing utilities.

Classes:
    * :py:class:`TimerException`
    * :py:class:`TimerTypeError`
    * :py:class:`TimerValueError`
    * :py:class:`TimerKeyError`
    * :py:class:`TimerCompatibilityError`
"""


__all__ = ['TimerException', 'TimerTypeError', 'TimerValueError',
           'TimerKeyError', 'TimerCompatibilityError']


class TimerException(Exception):
    """Base exception for invalid data in :py:class:`Timer`.

    A *name* and *dtype* are used as a pair, otherwise *msg* is used.

    Args:
        msg_or_data (str, optional): Error message or data name.
        dtype (obj, str, optional): Valid data.
    """
    def __init__(self, msg_or_name='', dtype=None):
        self.message = "{} is not a {}".format(msg_or_name, dtype) \
                       if dtype else msg_or_name
        super().__init__(self.message)


class TimerTypeError(TimerException):
    """Exception for invalid data type assigment in :py:class:`Timer`."""
    pass


class TimerValueError(TimerException):
    """Exception for invalid values in :py:class:`Timer`."""
    pass


class TimerKeyError(TimerException):
    """Exception for invalid key indexing in :py:class:`TimerDict`."""
    pass


class TimerCompatibilityError(TimerException):
    """Exception for incompatible :py:class:`Timer` instances.

    Args:
        message (str, optional): Error message.
    """
    def __init__(self, message=''):
        self.message = message if message else 'incompatible clocks'
        super().__init__(self.message)