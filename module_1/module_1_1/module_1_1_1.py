# ===============================
# Import helper from another file
# ===============================
from utils import helper
from utils import helper as h

# ===============================
# Base classes + inheritance
# ===============================

def check_variable_contain():
    x = "vau"
def check_nest_func():
    class OuterClass:
        class InnerClass:
            def __init__(self):
                pass
            def check():
                print("Checking")
    z(OuterClass)
    k = OuterClass()
    k.check()

def z(c):
    c()



class OuterClass:
    pass
class Mainclass:
    class NestedClass:
        class AnotherNestedClass:
            pass
        def __init__(self):
            var = "vaibhav"
        def speak_nested():
            f = MainClass()
            f.speak_main()

    d = NestedClass()
    h = OuterClass()
    def __init__(self):
        print("Hello World")
    def speak_main():
        class AnotherNestedClass2:
            pass

        c = NestedClass()
        c.speak_nested()
        print("main")
    

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        h()
        super().speak()
        print("Dog speaks")

class A:
    def speak(self):
        print("A")

class B(A):
    def speak(self):
        super().speak()
        print("B")

class C(B):
    def speak(self):
        super().speak()
        print("C")

# ===============================
# Static / Class method classes
# ===============================
class Cat:
    @staticmethod
    def purr():
        print("Cat purrs")

class User:
    @classmethod
    def from_dict(cls, data):
        print("User created from dict")

# ===============================
# File-level function
# ===============================
def file_func():
    print("File-level function called")

file_func()

# ===============================
# Function calling class methods
# ===============================
def run(data={}):
    User.from_dict(data)
    Cat.purr()

run()

# ===============================
# Function calling imported helper
# ===============================
def process():
    helper()
    h()

process()

# ===============================
# Class with all methods
# ===============================
class CovalentClass:
    def __init__(self):
        print("Constructor (__init__) called")
        self.setup()

    def setup(self):
        print("Setup called")

    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method called")

    @staticmethod
    def static_method():
        print("Static method called")

# ===============================
# Function calling everything
# ===============================
def function_calling_methods():
    file_func()
    obj = CovalentClass()
    obj.instance_method()
    CovalentClass.class_method()
    CovalentClass.static_method()

    def nested_inside_function():
        print("Nested function")
    nested_inside_function()

    return nested_inside_function

nested_func_ref = function_calling_methods()
nested_func_ref()

# ===============================
# Class calling function + nested
# ===============================
class AdvancedClass:
    def __init__(self):
        print("AdvancedClass constructor")

    def instance_calls_function(self):
        file_func()

        def nested():
            print("Nested in class")
        nested()
        return nested

adv_obj = AdvancedClass()
nested = adv_obj.instance_calls_function()
nested()

# ===============================
# Lambda
# ===============================
f = lambda x: x**2
print(f(5))

# ===============================
# Function as variable
# ===============================
def extra_func():
    print("Extra")

func_var = extra_func
func_var()

# ===============================
# Method as variable
# ===============================
obj = CovalentClass()
method_ref = obj.instance_method
method_ref()

# ===============================
# Function returning function
# ===============================
def outer():
    def inner():
        print("Inner")
    return inner

outer()()

# ===============================
# Function as argument
# ===============================
def executor(func):
    func()
    return outer
    

executor(file_func)

# ===============================
# Dict dispatch
# ===============================
def x():
    dispatch = {"run": run}
    dispatch["run"]()
    y = lambda x:x*x
    y(2)
def x3():
    obj = Animal()
    getattr(obj, "speak")()

# ===============================
# getattr dynamic call
# ===============================

# ===============================
# Recursion
# ===============================
def recursive(n):
    if n > 0:
        recursive(n-1)

recursive(2)

# ===============================
# Class method chaining
# ===============================
class ChainClass:
    @classmethod
    def a(cls):
        cls.b()

    @classmethod
    def b(cls):
        print("b called")

ChainClass.a()

# ===============================
# Static method calling function
# ===============================
class StaticCaller:
    @staticmethod
    def call_func():
        file_func()

StaticCaller.call_func()

# ===============================
# Decorator
# ===============================
def decorator(func):
    def wrapper():
        func()
    return wrapper

@decorator
def decorated_func():
    print("Decorated")
def call_decorated_func():
    decorated_func()

# ===============================
# Callable class
# ===============================
class CallableClass:
    def __call__(self):
        print("Called")

CallableClass()()

# ===============================
# Nested class inside function
# ===============================
def outer_func():
    class Inner:
        def method(self):
            file_func()
    Inner().method()
    Animal().speak()

outer_func()

# ===============================
# CLASS PASSING CASES
# ===============================
def class_executor(cls):
    obj = cls()
    obj.instance_method()

class_executor(CovalentClass)

def get_class():
    return CovalentClass

get_class()()

MyClass = CovalentClass
MyClass()

def call_class_methods(cls):
    cls.class_method()
    cls.static_method()

call_class_methods(CovalentClass)

def factory(name):
    return CovalentClass

factory("x")()

class Wrapper:
    def __init__(self, cls):
        self.cls = cls
    def create(self):
        return self.cls()

Wrapper(CovalentClass).create()

def create_and_call(cls):
    cls().speak()

create_and_call(Dog)

for cls in [CovalentClass, AdvancedClass]:
    cls()

{"cov": CovalentClass}["cov"]()

DynamicClass = type("DynamicClass", (), {
    "__init__": lambda self: print("Dynamic init")
})

def dynamic_class_call():
    DynamicClass()


# ===============================
# Class decorator
# ===============================
def class_decorator(cls):
    class Wrapped(cls):
        pass
    return Wrapped

@class_decorator
class DecoratedClass:
    def __init__(self):
        print("DecoratedClass init")

DecoratedClass()

# ===============================
# Metaclass
# ===============================
class Meta(type):
    def __call__(cls, *args, **kwargs):
        print("Meta call")
        return super().__call__(*args, **kwargs)

class MetaExample(metaclass=Meta):
    def __init__(self):
        print("MetaExample init")

def metaclass_call():   
    MetaExample()

# ===============================
# Advanced dynamic calls
# ===============================
file_func.__call__()
CovalentClass.instance_method(obj)

from functools import partial
def add(a, b): print(a+b)
partial(add, 5)(10)

def f1():
    def f2():
        def f3():
            print("deep")
        return f3
    return f2

f1()()()

globals()["file_func"]()

def local_call():
    def inner(): print("local inner")
    locals()["inner"]()

local_call()

def dynamic_method(self):
    print("dynamic method")

setattr(CovalentClass, "dynamic_method", dynamic_method)
obj = CovalentClass()
obj.dynamic_method()

eval("file_func()")
exec("file_func()")

def gen():
    yield 1

def generator_func():
    next(gen())

import asyncio
async def async_func():
    print("async")

asyncio.run(async_func())

# ===============================
# Property
# ===============================
class P:
    @property
    def x(self):
        print("property")
        return 1

_ = P().x

# ===============================
# Operator overload
# ===============================
class Add:
    def __add__(self, other):
        print("add called")

Add() + Add()

# ===============================
# Context manager
# ===============================
class Ctx:
    def __enter__(self):
        print("enter")
    def __exit__(self, *args):
        print("exit")

with Ctx():
    pass

# ===============================
# Iterator
# ===============================
class It:
    def __iter__(self): return self
    def __next__(self): raise StopIteration

for _ in It():
    pass

# ===============================
# Exception flow
# ===============================
def err():
    raise ValueError

try:
    err()
except:
    pass

# ===============================
# Chaining
# ===============================
class Chain:
    def a(self): return self
    def b(self): print("chain")


Chain().a().b()

# ===============================
# __new__
# ===============================
class New:
    def __new__(cls):
        print("new")
        return super().__new__(cls)

New()

# ===============================
# Multiple decorators
# ===============================
def d1(f):
    def w(): return f()
    return w

def d2(f):
    def w(): return f()
    return w

@d1
@d2
def multi():
    print("multi")

multi()

# ===============================
# SUPER usage
# ===============================
Dog().speak()
C().speak()


# class cov:
#     def __init__(k):
#         print("Hello World")

# def n():
#     print("lunch")

# def m(k):
#     x = cov()
#     n()
#     n()
#     return cov
