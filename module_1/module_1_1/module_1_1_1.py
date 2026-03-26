# ===============================
# File-level function calls
# ===============================

def file_func():
    print("File-level function called")

# Calling a file-level function directly
file_func()

# ===============================
# Class with all types of methods
# ===============================
class CovalentClass:
    def __init__(self):
        print("Constructor (__init__) called")
        self.instance_var = "Instance variable"

    # Instance method
    def instance_method(self):
        print("Instance method called")

    # Class method
    @classmethod
    def class_method(cls):
        print("Class method called")

    # Static method
    @staticmethod
    def static_method():
        print("Static method called")

# ===============================
# Function calling other functions and class methods
# ===============================
def function_calling_methods():
    print("Function calling class and functions")
    
    # Call file-level function
    file_func()
    
    # Call class constructor
    obj = CovalentClass()
    
    # Call instance method
    obj.instance_method()
    
    # Call class method
    CovalentClass.class_method()
    
    # Call static method
    CovalentClass.static_method()
    
    # Nested function inside this function
    def nested_inside_function():
        print("Nested function called")
    nested_inside_function()  # Call nested function

    # Return nested function for calling outside
    return nested_inside_function

# Call function that calls methods
nested_func_ref = function_calling_methods()
nested_func_ref()  # Calling nested function outside

# ===============================
# Class method calling function and nested function
# ===============================
class AdvancedClass:
    def __init__(self):
        print("AdvancedClass constructor called")

    def instance_calls_function(self):
        print("Instance calls function")
        file_func()  # Function call from class method

        # Nested function inside class method
        def nested_in_class():
            print("Nested function inside class method called")
        nested_in_class()
        return nested_in_class

# Call class and its methods
adv_obj = AdvancedClass()
nested_from_class = adv_obj.instance_calls_function()
nested_from_class()  # Call nested function returned from class method

# ===============================
# Lambda function calls
# ===============================
f = lambda x: x**2
print("Lambda function called:", f(5))

# ===============================
# Chained calls / combinations
# ===============================
def combination_calls():
    print("Combination calls")
    
    # Call function inside another function that calls class
    def inner_function():
        print("Inner function")
        obj = CovalentClass()
        obj.instance_method()
        CovalentClass.class_method()
        CovalentClass.static_method()
    inner_function()

combination_calls()