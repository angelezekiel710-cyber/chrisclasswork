     #WRITING FUNCTIONS
def welcome():
    print("Welcome to python programming! ")
welcome()

 #PARAMETERS
def greet(name):
    print(f"Hello! {name}")
greet("Destiny")

 #RETURN VALUES
def multiply(a,b):
    return(a*b)
result = multiply(20,17)
print(result)

# #SCOPE
#"The code did not run. it will produce an error
#because print('age') tries to access age outside the function
#and age is a local variable so it cannot be accessed outside
#the function

#UNIT TESTING
def show():
    age = 20

show()
print(age)


