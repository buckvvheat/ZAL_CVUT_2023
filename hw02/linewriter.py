STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text."
  
def writeTextToFile(h):
    with open('fileineed.txt', 'w') as out:
        out.write(STATICKY_TEXT + " " + str(h))
        nameofafile = 'fileineed.txt'
    return nameofafile