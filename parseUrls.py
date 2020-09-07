'''
    Created by: Lirh
    Date: 6 September 2020
    reason: Remove [.] from malware url list and save it into new file
'''
class readFileAndSaveData():
    def __init__(self, file):
        self.file = file
        self.arr = []
        self.new_arr = []

    #Function just only for read the file and save it on self.arr
    def readFile(self): 
        try:
            malwareList = open(self.file, 'r')
            for line in malwareList.readlines():
                self.arr.append(line)
        except:
            print('\n [!] There was an error opening the file')

    #Function for parse the data, replacing [.] for .
    def parseArr(self):
        for x in range(len(self.arr)):
            text = self.arr[x]
            self.arr[x] = text.replace('[.]', '.')

    #Function for replacing hxxp for http or https
    def httpOrHttps(self):
        cad = ['http://', 'https://']
        for x in range(len(self.arr)):
            if self.arr[x][4] == 's':
                self.new_arr.append(cad[1] + self.arr[x][7:])
            else:
                self.new_arr.append(cad[0] + self.arr[x][6:])

    #Function for save the data in a New File ready for be blocked                
    def saveInNewFile(self, fileOutput):
        try:
            file = open(fileOutput, 'w')
            for x in range(len(self.new_arr)):
                file.write(self.new_arr[x])
            
            print('File Created, Job Done')
        except:
            print('\n[!] There was an error creating or writing the File')


if __name__ == '__main__':
    fileInput = str(input('[*] Enter the name of the input File : '))
    fileOutput = str(input('[*] Enter the name of output File : '))
    Data = readFileAndSaveData(fileInput)
    Data.readFile()
    Data.parseArr()
    Data.httpOrHttps()
    Data.saveInNewFile(fileOutput)


