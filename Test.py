    
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
