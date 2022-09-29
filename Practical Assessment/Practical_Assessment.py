#Practical Assessment

# added a comma separated file into the project folder and named it "marks" which is an excel spreadsheet that consists of three values assigned to 50 different people (arrays). The lists are forenameList, surnameList and scoreList.

#libraries 
import csv

#list defintions
forenameList = []
surnameList  = []
markList    = []


#methods
def fillLists():
    with open("marks.csv", "r") as csvFile:
        csvReader = csv.reader(csvFile) # created a variable called csvReader which will use the csv library and read the csvFile, returning the data.
        for row in csvReader:
            surnameList.append(row[0])
            forenameList.append(row[1])
            markList.append(int(row[2]))
        #end for
    #end with
    return forenameList, surnameList, markList
#end fillLists

def findMaximum(markList):
    maxMark = None
    maxPosition = None
    if len(markList)>0:
        maxMark = markList[0]
        for index in range (len(markList)):
            if markList[index] > maxMark:
                maxMark = markList[index]
                maxPosition = index
            #end if
        #end for
    #end if
    print (maxMark, "at position ", maxPosition)
    return maxMark, maxPosition
#end findMaximum

def writeToFile(maxMark,maxPosition):
    #write to file Highest Mark
    studentName = forenameList[maxPosition] + " " + surnameList[maxPosition]
    print (studentName + " had the highest mark of " + str(maxMark))
    with open ("highestMark.txt","w") as f:
        f.write(studentName + " had the highest mark of " + str(maxMark))
    #end with
#end writeToFile


#main program
surnameList, forenameList, markList = fillLists()
maxMark, maxPosition = findMaximum(markList)
writeToFile(maxMark, maxPosition) 
