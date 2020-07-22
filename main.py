#functions are yoused to oginize code,you need to deffin and call

def greeting(name):
   print("hello "+ name)
  



gustname = input("what is your name:")

greeting(gustname)

def addnums(num1, num2):
  print(num1+num2)


def subnums(num1, num2):
  print (num1-num2)



  
num2 = int(input("give me a number:"))
num1 = int(input("give me a number:"))
operator = input("add or sub:")

if operator.lower() == "add":
  addnums(num1,num2)  
elif operator.lower() == "sub":
  subnums(num1, num2)
else:
  print("that's not an opsin")
