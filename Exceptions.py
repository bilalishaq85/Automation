from Hybris.Lib.LogConfig import Logger


class SaunterExceptions(Exception):
    """Base class for exceptions in this module."""
    pass


class TimeoutException(SaunterExceptions):
    def _get_message(self):
        Logger.logr.errormsg(self._message)

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class ElementNotFound(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class ElementVisiblityTimeout(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class ElementTextTimeout(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class InvalidLocatorString(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class WindowNotFound(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class ProfileNotFound(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)


class ProviderException(SaunterExceptions):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message

    message = property(_get_message, _set_message)
