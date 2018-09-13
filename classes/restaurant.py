class Restarant():
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print('Restarant: {} \n Type of food: {}'.format(self.name,self.cuisine))
