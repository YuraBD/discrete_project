"""
Modificated list. The only reason I created it is to make simple printing
"""


class ModificatedList:
    def __init__(self):
        self._lst = []

    def __str__(self):
        out_str = ''
        for letter in self._lst:
            out_str += letter.__str__()
            out_str += ': '
            out_str += str(letter.get_digit())
            out_str += ', '
        return out_str

    def append(self, value):
        self._lst.append(value)

    def is_containing_digit(self, digit):
        for letter in self._lst:
            if letter.digit == digit:
                return False
        return True

    def num_possible(self, letter):
        return 10 - len(self._lst)

    def pop(self):
        return self._lst.pop()

    def __getitem__(self, index):
        return self._lst[index]

    def __contains__(self, item):
        if item in self._lst:
            return True
        return False

    def __len__(self):
        return len(self._lst)
