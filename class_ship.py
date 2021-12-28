import random 
class Ship:
    
    maxcrewMembers = 80
    
    def __init__(self, name, typeShip, decksCount, velocity, maxcrewMembers):
        self.__name = name
        self.set_typeShip(typeShip)
        self.set_decksCount(decksCount)
        if decksCount < 1:
            raise ValueError('The decksCount should be more 1')
        self.__velocity = velocity
        self.__maxcrewMembers = maxcrewMembers 
            
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name     
    
    def get_typeShip(self):
        return self.__typeShip
    
    def set_typeShip(self, typeShip):
        self.__typeShip = typeShip
        if self.__typeShip == 'Burk':
            self.__mastCount = 3
            self.__sailsCount = 12
        elif self.__typeShip == 'Brig':
            self.__mastCount = 2
            self.__sailsCount = 8
        else:
            self.__mastCount= 1
            self.__sailsCount = 4
            
    def whistleEveryoneUpr(self, maxcrewMembers):
        return self.__maxcrewMembers / 2  #предположим что количество членов экипажа поровну в трюме и на палубе
        
    def boarding(self, maxcrewMembers):
        return self.__maxcrewMembers - random.randint(1, maxcrewMembers) #в процессе захвата судна гибнет случайное число членов экипажа    

    def get_decksCount(self):
        return self.__decksCount
    
    def set_decksCount(self, decksCount):
        self.__decksCount = decksCount
        if self.__decksCount == '1':
            self.__gunsCount = 16
        if self.__decksCount == '2':
            self.__gunsCount = 32
    
    def get_mastCount(self):
        return self.__mastCount 
    
    def get_gunsCount(self):
        return self.__gunsCount
    
    def get_sailsCount(self):
        return self.__sailsCount
    
    def get_velocity(self):
        return self.__velocity
    
    def set_velocity(self, velocity):
        self.__velocity = velocity  
     

    
    name = property(get_name, set_name)
    typeShip = property(get_typeShip, set_typeShip)
    decksCount = property(get_decksCount, set_decksCount)
    mastCount = property(get_mastCount)
    gunsCount = property(get_gunsCount)
    sailsCount = property(get_sailsCount)
    velocity = property(get_velocity, set_velocity)
    
    
try:
    ship1 = Ship("BlackPearl", 'Brig', 0, 5, 80)
except ValueError:
    ship1 = Ship("BlackPearl", 'Brig', 2, 5, 80)


print(f'Название корабля - {ship1.name}')    
print(f'Тип корбаля - {ship1.typeShip}')
print(f'Свистать {ship1.whistleEveryoneUpr(80)} человек наверх')
print(f'Выжило {ship1.boarding(80)} членов экипажа в процессе взятия на абордаж')
ship1.name = 'FlyingDutchman'
print(f'Корабль переименован в {ship1.name}')