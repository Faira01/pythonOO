"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start=0):
        """Makes new generator, starting at start"""
        self.start = start

    def ___ref___(self):
        """Shows representation"""

        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        """Returns next number"""
        self.start += 1

        return self.start - 1
         

    def reset(self):
        self.start