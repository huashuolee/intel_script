
def left(phrase):
    print phrase
    str1 = ','.join(phrase)
    print type(str1)
    str2 = str1.replace("right","left")
    print str2

if __name__ == "__main__":
    left(("left","right","left","stop",))
