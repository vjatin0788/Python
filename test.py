#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:30:42 2017

@author: jitan
"""

class Myclass(object):
    var = "Puri"
    __hiddenvar = 'my hidden var'
    def __new__(cls,*args,**kwargs): #this is the method which create the objects
        print(cls)
        print(args)
        print(kwargs)
        obj = super().__new__(cls) #This is how implicitly object is created.
        return obj
    def __init__(self,name):   #init is not constructor it is method but it is called as class is called to initialize the object
        self.name = name
    def display(self):
        print(self.name)
        print("%s display called" % self.name)
    @staticmethod    
    def stat_method():    
        print("static method")
    @classmethod # class method is method in which class itself is passed 
    def static(cls):
        print(cls)
    def __repr__(self):
        return self.name
    def __str__(self):
        return 'my name : %s' % self.name
        
def main():
    obj = Myclass("Jatin")        
    obj.display() #implicitly Myclass.display(obj)
    Myclass.display(obj)
    print(obj._MyClass__hiddenvar) #accessing the hidden var
    print(Myclass.display) # it is function type. it will tell its type 
    print(Myclass.stat_method()) #it is static method
    print(obj.display) #it is method type because obj is passed
    print(obj.stat_method) # it is function type not method type becz it is static
    Myclass.var="hello"
    print(obj.var)
    obj.var="world"
    print(Myclass.var)
    Myclass.var="hello world"
    print(obj.var)
    Myclass.static()
    
#define the main method here.
if __name__ == "__main__":
    main()
    
    
