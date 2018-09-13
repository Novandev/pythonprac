from datetime import date
class Person(object):
    ''' This class will take a persons information and write it down to a file'''
    def _init_(self,name,occupation,date_created):
        self.name = name
        self.occupation = occupation
        self.date_created = date.today()
    def showInfo(self):
        print('Name is :{} \n Occupation: {} \n This persons info was stored at {}'.format(self.name,self.occupation,self.date_created))
