#Global Set
D = set()

#getting list of all file names in folder
def getFileNamesListInDirectory(inputPath):
        import glob
        # inputPath param example: './test/'
        return glob.glob(inputPath + '*.html')
    
def readTextInFile(path):
        with open(path, 'r', encoding="utf8") as myfile:
            data = myfile.read().replace('\n', '')
            return data

def extractGeorgianWords(s):
        import re
        matches = re.findall('([ხელმძღქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*-[ქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*)|([ხელმძღქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*)', s, re.DOTALL)
        res = [(' ' + str(i[1]) + ' ') for i in matches if (len(str(i[1])) > 0)]
        return res
 
def getGeoWordsFromFiles(inputPath):   
        files = getFileNamesListInDirectory(inputPath)
        for file in files:
            doc = readTextFile(file)
            georgianOnly = extractGeorgianWords(doc)
            for word in georgianOnly:
                D.add(word)
        
#must have alreade created output file (output.txt)
def save2file(filename):
        import io
        with open(filename, 'w', encoding="utf8") as f:
           for s in D:
               f.write(s + '\n')
    
#run this function to generate GeoWords DataBase from files in catalof    
#inputPath - path to folder where located html files
#outputPath - path to file where will have to be written extracted georgian words
def generateGeoWordDB(inputPath, outputPath):
    getGeoWordsFromFiles(inputPath)
    save2file(outputPath)
