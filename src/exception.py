class QuoridorException(Exception):
    pass


class OutOfBoardException(QuoridorException):
    pass


class UnknownActionException(QuoridorException):
    pass
