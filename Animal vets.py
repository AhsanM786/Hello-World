from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Animal"


    #Methods
    @abstractmethod
    def eat(self):
        pass

    def reproduce(self):
        return("I Lay Egss")
        

    def sleep(self):
        return("I am sleeping now")

    def type(self):
        return(self.value)

class Antelope(Mammal):
    #Attributes

    #Constructors
    def __init__(self):
        self.value = "Antelope"

        #Methods
        def type(self):
            return(self.value)

            def eat(self):
                return "I eat grass"

class Bear (Mammal):
    #Attributes

    BearFoodNow = None
    BearFood = ["Chicken", "BigFish", "Bug", "Cow", "Leaves", "Sheep"]
    Chicken = True
    BigFish = True
    Bug = True
    Cow = True
    Leaaves = True
    Sheep = True

    #Constructors

    def __init__(self):
        self.value = "Bear"

        #Methods
        def type(self):
            return(self.value)

            def eat(self):
                return list ["Chicken", "BigFish", "Bug", "Cow", "Leaves", "Sheep"]



    









class Cat(Mammal):
    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Cat"


    #Methods
    def type(self):
        return(self.value)
    
    def eat(self):
        return "I eat mice"

class Dog(Mammal):
     #Attributes

    color = None


    #Constructors
    def __init__(self):
        self.value = "Dog"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat meat"

class Budgie(Bird):
    #Attributes

    BeakColour = None

    #Constructors
    def __init__(self):
        self.value = "Budgie"

    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat worms"

class Parrot(Bird):
    #Attributes

    BeakColour = None

    #Constructors
    def __init__(self):
        self.value = "Parrot"

    #Methods
        def type(self):
            return(self.value)

        def eat(self):
            return "I eat crumbs"

class Reptile(Animal):

    #Constructors
    def __init__(self):
        self.value = "Reptile"

    #Attributes

    #Methods
    def reproduce(self):
        return("I lay eggs myself")
    
class Gecko(Reptile):
    #Constructors
    def __init__(self):
        self.value = "Reptile"

    #Methods
    def reproduce(self):
        return("I lay eggs myself")

class Turtoise(Reptile):
    #Attributes

    #Consructors
    def __init__(self):
        self.value = "Reptile"

    #Methods
    def eat(self):
        return "I eat vegetables"
        
class Plant(ABC):

    #Constructors 
    def __init__(self):
        self.value = "Plant"

    #Methods
    @abstractmethod
    def Grass(self):
        pass
    
    def Leaves(self):
        pass

class Grass (Plants):

    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Grass"

    #Methods
    

        
        


