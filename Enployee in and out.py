class Employee():
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("Creating object...")
    obj=Employee()
    del obj
    print("Function end...")
    
print("Calling Create_obj()...")
obj=Create_obj()
print("Programme end")
