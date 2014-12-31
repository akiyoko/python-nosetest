class Calculator(object):
    def __init__(self, num1):
        self.num1 = num1

    def add(self, num2):
        if num2 is None:
            raise Exception("Arg should not be None.")
        return self.num1 + num2
