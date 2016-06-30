"""pyGreek-prank.

Usage:
  pygreek.py prank <FILENAME>... [-vds]
  pygreek.py deprank <FILENAME>... [-vds]
  pygreek.py (-h | --help)
  pygreek.py --version

Options:
  -s --space    Also changes the whitespace to different whitespace
  -h --help     Show this screen.
  -d --dest     Does not save backup of text
  --version     Show version.
"""
import docopt
import os
import codecs

def createErrors(filename):
    originalFile = codecs.open(filename,mode="r+",encoding='utf-8')
    contents = originalFile.read()
    if not(args["--dest"]):
        if os.path.isfile(filename+".bak"):
            os.remove(filename+".bak")
        bakFile = codecs.open(filename+".bak",mode="w",encoding="utf-8")
        bakFile.write(contents)
        bakFile.close()
    newcontents = contents.replace(";",u"\u037E")
    if args["--space"]:
        newcontents = newcontents.replace(" ",u"\u2005")
    originalFile.close()
    os.remove(filename)
    probFile = codecs.open(filename,mode="w",encoding="utf-8")
    probFile.write(newcontents)
    if args["--space"]:
        print "Changed Semicolons and whitespaces for " + args["<FILENAME>"][i]
    else:
        print "Changed Semicolons for " + args["<FILENAME>"][i]

def removeErrors(filename):
    originalFile = codecs.open(filename, mode="r+", encoding='utf-8')
    contents = originalFile.read()
    if not(args["--dest"]):
        if os.path.isfile(filename + "prob_.bak"):
            os.remove(filename + "_prob.bak")
        bakFile = codecs.open(filename + ".bak", mode="w", encoding="utf-8")
        bakFile.write(contents)
        bakFile.close()
    newcontents = contents.replace(u"\u037E",";")
    if args["--space"]:
        newcontents = newcontents.replace(u"\u2005"," ")
    originalFile.close()
    os.remove(filename)
    fixedFile = codecs.open(filename, mode="w", encoding="utf-8")
    fixedFile.write(newcontents)
    if args["--space"]:
        print "Changed Greek Question Mark and whitespaces for " + args["<FILENAME>"][i]
    else:
        print "Changed Greek Question Mark for " + args["<FILENAME>"][i]


if __name__=="__main__":
    args = docopt.docopt(__doc__)
    #print args
    if args["prank"]:
        for i in range(len(args["<FILENAME>"])):
            createErrors(args["<FILENAME>"][i])

    else:
        for i in range(len(args["<FILENAME>"])):
            removeErrors(args["<FILENAME>"][i])
