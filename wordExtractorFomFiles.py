#getting list of all file names in folder
def getFileNamesListInDirectory():
    import glob
    return glob.glob('./test/*.html')
    
    
def readTextFile(path):
    with open(path, 'r', encoding="utf8") as myfile:
        data = myfile.read().replace('\n', '')
        return data

def extractGeorgianWords(s):
    import re
    matches = re.findall('([ხელმძღქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*-[ქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*)|([ხელმძღქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*)', s, re.DOTALL)
    res = [(' ' + str(i[1]) + ' ') for i in matches if (len(str(i[1])) > 0)]
    return res
 
def getGeoWordsFromFiles():   
    files = getFileNamesListInDirectory()
    for file in files:
        doc = readTextFile(file)
        georgianOnly = extractGeorgianWords(doc)
        print(georgianOnly)



