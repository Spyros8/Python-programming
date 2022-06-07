import random
import abc
from io import StringIO

#NOTE:  require  google cloud payment and enabling the cloud Build API
#Then initialise App Engine App with my project using
# gcloud app create --project=[YOUR_PROJECT_ID]
#import myappengine

#NOTE: remember continue break and pass

class MyClass(object):
    var = 10

this_obj = MyClass()
print(this_obj.var)
that_obj = MyClass()
print(that_obj.var)

#NOTE: self is the id an instance gives when we try to print it + hexcode [address in memory]
#NOTE: Instance.method(): pass instance as first argument
class Joe(object):
    def callme(self):
        print("calling callme method with instance: ")

thisjoe = Joe()
thisjoe.callme()

#NOTE: use init constructor
#NOTE: Initialising object
#NOTE: Look at exception handling again
class MyNum(object):
    #NOTE: in init constructor add attributes
    def __init__(self, value = 6):
        try:
            value = int(value)
            self.val = value
        except ValueError:
        #NOTE: Here make less redundant
            value = 0
            self.val = value
        finally:
            print("calling __init__")

    def increment(self):
        self.val += 1

dd = MyNum(value ='hi')
dd.increment()
dd.increment()
print(dd.val)


#NOTE: Can use del() to delete object in python
class YourClass(object):
    classy = 10
    insty = 5

    def set_val(self):
        self.insty = self.classy

dd = YourClass()

dd.set_val()
print(dd.classy)
dd.insty = 50
dd.set_val()
print(dd.insty)
del dd.insty
print(dd.insty)


####ASSIGNMENT 1#######
import assignments
from assignments import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")
print(a.get_list())
print(b.get_list())



#NOTE:Inheritance
#object.attribute lookup hierarchy (instance, class (subclass) and super class)
class Date(object):
    def get_date(self):
        return "2014-10-13"

class Time(Date):
    def get_time(self):
        return "08:13:07"

dt = Date()

tm = Time()
print(tm.get_time())
print(tm.get_date())

#Example: In inheritance hierarchy can avoid duplicating code
#NOTE: Remember super__init__ from MSc AI and practice
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s." % (self.name, food))

#NOTE: Specific vs common functionalities
class Dog(Animal):
    
    def __init__(self, name):
        super(Dog, self).__init__(name) #NOTE: Common functionality
        self.breed = random.choice(["Shih Tzu", "Beagle", "Mutt"]) #NOTE: Specific functionality
    def fetch(self, thing):
        print("%s goes after the %s!" % (self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print("%s shreds the string!" % (self.name))

r = Dog("Rover")
f = Cat("Fluffy")

r.fetch("paper")
f.swatstring()
r.eat("dog food")
f.eat("cat food")

d = Dog("dogname")

print(d.name)
print(d.breed)


#NOTE: Check for multiple inheritance how it works

class A(object):

    def dothis(self):
        print("doing this in A")

class B(A):
    pass

class C(object):

    def dothis(self):
        print("doing this in C")

class D(B, C):
    pass

d_instance = D()
d_instance.dothis()

print(D.mro())

#NOTE: Abstract class

class GetterSetter(object):
    __metaclass__=abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, input):
        """Set a value in the instance."""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from the instance."""
        return

class MyClass(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

x = MyClass()
print(x)


#NOTE: Method overloading and extending

class GetSetParent(object): #NOTE: abstract class but contains methods that can be inherited and used by child classes
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        self.val = 0
    def set_val(self, value):
        self.val = value
    def get_val(self):
        return self.val
    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value) #NOTE: Go via super class to reinstantiate val
    def showdoc(self):
        print("GetSetInt object ({0}), only accepts"
              "integer values".format(id(self)))

class GetSetList(GetSetParent):
    def __init__(self, value = 0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print("GetSetList object, len {0}, stores"
              "history of values set".format(len(self.vallist)))

x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()


#NOTE:Composition [less dependency than for inheritance]

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer
    def write(self):
        write_text = "this is a silly message"
        self.writer.write(write_text)


fh = open("test.txt", "w")
w1 = WriteMyStuff(fh) #NOTE:Writes to files
w1.write() 
fh.close()

sioh = StringIO() #NOTE: Writes to string buffer
w2 = WriteMyStuff(sioh)
w2.write()

print("file object: ", open("test.txt", "r").read())
print("StringIO object: ", sioh.getvalue())


#####Assignment 2######

from assignments import LogFile, DelimFile, Write_File_new, CSVFormatter, LogFormatter

log = LogFile("log.txt")
c = DelimFile("text.csv", ",")

log.write("this is a log message")
log.write("this is another log message")

c.write(["a", "b", "c"])
c.write(['1', '2', '3', '4'])


writecsv = Write_File_new("text2.csv", CSVFormatter)
writelog = Write_File_new("log2.txt", LogFormatter)

writecsv.write(["a", "b, 2", "c", "d"])
writelog.write("this is another log message")

writecsv.close()
writelog.close()


















