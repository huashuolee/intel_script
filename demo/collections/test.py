import collections
import sys


def checkio(text):
    str.lower(str(text))
    #replace this for solution
    c = collections.Counter()
    c.update(text)
    most_wanted = c.most_common()[0][0]
    print most_wanted
    print c.most_common()
    print c.most_common().sort()
if __name__=="__main__":
    checkio(str(sys.argv[1:]))
