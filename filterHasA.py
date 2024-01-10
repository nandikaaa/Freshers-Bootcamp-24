class ConsoleDisplayController:
    __content = '' 
    
    def setContent(self, array):
        self.__content = array
        
    def display(self):
        for item in self.__content:
            print(item)
        
class StartsWithStrategy:
    __startsWith = ''
    
    def setStartsWith(self, key):
        self.__startsWith = key
        
    def invoke(self, item):
        return item[0] == self.__startsWith

class StringFilterController:
    __result = []
    objSS = StartsWithStrategy()
    objSS.setStartsWith('u')
    def setList(self, stringList):
        self.stringList = stringList
    
    def filter(self):
        for string in self.stringList:
            if self.objSS.invoke(string):
                self.__result.append(string)
        
    def getList(self):
        return self.__result


list_sample = ["apple","ball","cat","umbrella"]
consoleObj = ConsoleDisplayController()
filterObj = StringFilterController()
filterObj.setList(list_sample)
filterObj.filter()
consoleObj.setContent(filterObj.getList())
consoleObj.display()
