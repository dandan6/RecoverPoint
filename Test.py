import sys


class Tee(object):
    def __init__(self, input_handle, output_handle):
        self.input = input_handle
        self.output = output_handle

    def readline(self):
        result = self.input.readline()
        self.output.write(result)

        return result


if __name__ == '__main__':
    if not sys.stdin.isatty():
        sys.stdin = Tee(input_handle=sys.stdin, output_handle=sys.stdout)

    a = input('Type something: ')
    b = input('Type something else: ')
