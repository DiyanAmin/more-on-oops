#Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)
class find_numbers:
    def processer(self,numbers,total_number):
        noname={}
        for index,i in enumerate(numbers):
            if total_number-numbers in noname:
                return (noname[total_number-numbers,index])
            noname[numbers]=index
n=(10,20,30,40,50,60,70)
val=int(input('What value do you want to search: '))
print('Searching....')
result=find_numbers().processer(n,val)
print('Index 1 = %d,Index 2 = %d'%result)