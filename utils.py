class Utils:
    @staticmethod
    def reversed(number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        reversed_number = int(str(number)[::-1])
        return reversed_number

    @staticmethod
    def formatter(number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        binary_format = (bin(number))
        octal_format = (oct(number))

        binary_format = binary_format[2:]

        return binary_format, octal_format
