

def greet_programmer():
    print("Hello, programmer")
    greet_programmer()

def greet(name):
    name ="Brian"
    print(f"Hello World, {name}")
    greet()

def greet_with_default(name="programmer"):
    print("Hello"+ name)
    greet_with_default()

def add(num1, num2):
    num1=12
    num2=13
    total=num1+num2
    print(total)
    add()

def halve(number):
   div= number/2 
   print(div)

   halve()

