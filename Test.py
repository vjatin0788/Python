    
#array in python    
mylist = {1,2,3}  
ml1 = [x+1 for x in mylist]  #syntax

#function/methods are objct in python
def method1():
    return 'hello world';
def method2(method):
     methodToRun = method()
     print(methodToRun)
#methods act like objects.
method2(method1)

#key valuue
Map = {'a':1,'b':2}     
Map['a']

#Lambda Expression
double = lambda x : x * 2 #it can accept any number of arguments and it will always return the statement.
print(double(10))

#python iterator & generator
class listClass:
    
    def __init__(self,max):
        self.max = max
     
    def __iter__(self): #initialize the iterator
         self.start = -1
         self.inc = 1
         return self
    def __next__(self): #next method is called to get the next item
        if self.start > self.max :
             raise StopIteration  
        self.start = self.start + self.inc
        return self.start
        
   for i in listClass(10):
       print(i)
#generators are iterators  

def customGen(max):
    a = 0
    itr =1
    for i in range(a,max,itr):
        yield i #it creates the iterator and will stop the flow and go to the where function is called and when next method is called the 
                #flow return back here and continue untill new yield or return statement encounters.
    
gen = customGen(10)  #the arguments (max has a value of 10) are bound to names but the body of the function is not executed. Rather a generator-iterator object is returned as shown by the value of gen
next(gen)  

#looping 
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))   #else is printed when condition fails and when continue is used but not on break.

#Now the else will work on 
for i in range(1, 10):
    if(i%2==0):
        continue
    if(i == 9) :
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
 
# example of what we learn above
def tuble_ex():
    """ return defined t tuble"""
    t = (1,2,3)
    return t

a,b,c = tuble_ex() #it will unpack into three variables
print(a,b,c)   
    
#nested function
def square():
    """ return square of value """
    def add():
        """ add two local variable """
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())   

#Anonymous functions in python
#they are like lambda function with more number of argument.
number_list = [1,2,3]
y = map(lambda x:x**2,number_list)
print(list(y)) #1,4,9

# iteration example
name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration
print(*it)         # print remaining iteration

#zip and unzip
listA = [1,2,3,4]
listB = [5,6,7,8]
listC = [5,6,7,8]
z = zip(listA,listB,listC)
print(list(z))
z_list = list(z)
#unzip
un_zip = zip(*z_list)
u_listA,u_listB,u_listC = list(un_zip)
print(u_listA)

# Example of list comprehension
num1 = [1,2,3]
num2 = [i + 1 for i in num1 ]
print(num2)

# Conditionals on iterable
num1 = [5,10,15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]
print(num2)

