class Letter:
    """
    Letter class.
    """

    def __init__(self, str_value):
        self._str_value = str_value
        self.digit = None

    def __str__(self):
        return self._str_value

    def __repr__(self):
        return self._str_value

    def set_digit(self, digit):
        self.digit = digit

    def get_digit(self):
        return self.digit
