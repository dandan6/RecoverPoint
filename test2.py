import sys
import subprocess


##=============================================================================
class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()


f = open('out.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)
##=============================================================================
print('This works good, prints all the output to both console and to a file')
print("This does not print output to file in case of syntax errors")
print("This does not print output of subprocess.call")
