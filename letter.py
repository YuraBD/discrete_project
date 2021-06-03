class Letter:
    def __init__(self, str_value):
        self._str_value = str_value
        self.checked = []
        # self.counter = 0
        self.digit = None
    def __str__(self):
        return self._str_value

    def __repr__(self):
        return self._str_value

    def set_digit(self, digit):
        self.digit = digit
        self.checked.append(digit)

    def get_digit(self):
        return self.digit

    # def add_to_checked(self, digit):
    #     self.checked.append(digit)

