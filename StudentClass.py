from datetime import date

class Student: 
    def __init__(self,student_id,name,dob,classification):
        self.__student_id = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    def calc_age(self):
        today = date.today()
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = today.year - dob_year

    def calc_register(self):
        if self.__classification == "Sr":
            self.__register = '4/1 thru 4/3'

        elif self.__classification == "Jr":
            self.__register = '4/4 thru 4/6'

        elif self.__classification == "S":
            self.__register = '4/7 thru 4/9'

        elif self.__classification == "F":
            self.__register = '4/10 thru 4/12'

        else:
            self.__register = 'classification not found'
    
    def get_age(self):
        return self.__age

    def get_register(self):
        return self.__register