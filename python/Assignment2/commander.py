# MY STUDENT NUMBER

from astronaut import Astronaut

class Commander(Astronaut):

    '''
    Commander class represents astronauts that have commanded shuttle missions. The class extends the 
    Astronaut class by adding a boolean to represent if the commander is qualified to dock to ISS. 

    issDockingQualified - boolean representing whether the pilot is qualified to dock to ISS
    '''

    def __init__(self, name, dob, previousMissions, issDockingQualified):

        if type(issDockingQualified) != bool:
            raise ValueError("ISS Docking Qualified should be a boolean value")
        
        super().__init__(name, dob, previousMissions)
        self._issDockingQualified = issDockingQualified

    def __str__(self):
        return "%s ISS Qualified: %r" % (super().__str__(), self._issDockingQualified)

    def getISSDockingQualified(self):

        return self._issDockingQualified
    
    def setISSDockingQualified(self, issDockingQualified):

        if type(issDockingQualified) != bool:
            raise ValueError("ISS Docking Qualified should be a boolean value")
        
        self._issDockingQualified = issDockingQualified

    issDockingQualified = property(getISSDockingQualified, setISSDockingQualified)

if __name__ == "__main__":
    
    try:
        johnYoung = Commander("John Young", "", ['Gemini 3','Gemini 10', 'Apollo 10', 'Apollo 16'], True)
        print(johnYoung)
        johnYoung.issDockingQualified = False
        print(johnYoung.issDockingQualified)
        print(johnYoung)
    except ValueError as ex:
        print(ex)