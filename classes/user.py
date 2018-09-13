class User():
    def __init__(self,username,password,age):
        self.username = username
        self.password = password
        self.age = age
    def describe_user(self):
        print('{}\n{}\n{}\n'.format(self.username, self.password, self.age))
    def greet_user(self):
        print('hello {}'.format(self.username))
