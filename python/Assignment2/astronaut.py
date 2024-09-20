# MY STUDENT NUMBER

class Astronaut(object):
    '''
    Overarching astronaut class to capture common features across all shuttle astronauts. 
    Manages three instance variables:
    - name - immutable name of the astronaut 
    - dob - immutable date of birth of the astronaut
    - previousFlights - list of previous flights carried out by astronaut
    '''
    def __init__(self, name, dob, listOfFlights):

        if type(name) != str:
            raise ValueError("Name must be a string.")
        
        if type(dob) != str:
            raise ValueError("DOB must be a string.")
        
        if type(listOfFlights) != list:
            raise ValueError("listOfPreviousFlights must be a list.")
        
        self._name = name
        self._dob = dob
        self._previousFlights = listOfFlights

    def __str__(self):
        previousFlights = ""
        for flight in self._previousFlights:
            previousFlights = previousFlights + " " + flight

        return ("Name: %s DOB: %s Flights: %s" % (self._name, self._dob, previousFlights))
    
    def getName(self):
        return self._name

    def getDob(self):
        return self._dob

    def getPreviousFlights(self):
        return self._previousFlights

    def setPreviousFlights(self, previousFlights):
        if type(previousFlights) != list:
            raise ValueError("PreviousFlights must be list")
        
    name = property(getName)
    dob = property(getDob)
    previousFlights = property(getPreviousFlights, setPreviousFlights)
        
if __name__ == "__main__":

    try:
        neilArmstrong = Astronaut("Neil Armstrong", "August 5, 1930", ["Gemini 8"])
        print(neilArmstrong)
        neilArmstrong.previousFlights = ['Gemini 8', 'Apollo 11']
        print(neilArmstrong.name, neilArmstrong.dob, neilArmstrong.previousFlights)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try: 
        test1 = Astronaut(123, "August 5, 1930", ["Gemini 8"])
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
    
    try: 
        test2 = Astronaut("Neil Armstrong", 123, ["Gemini 8"])
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

    try: 
        test3 = Astronaut("Neil Armstrong", "August 5, 1930", 123)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)