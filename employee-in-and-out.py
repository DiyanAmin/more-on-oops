#Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
class Employee:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print('Deleted the object')
def process():
    object=Employee('No name')
    print(f'[nO TEXT]: {object.name}')
    print('Deleting....')
deletion=process()
#Placeholder