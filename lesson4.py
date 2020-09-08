
# in this case you always should close opened files
# "r" read mode, "w"- wite mode 
f = open("./user_name.txt", "r")
user_name = f.read()

f.close()
print(user_name)


f = open("./user_name.txt", "w")
f.write("Python file thing")

f.close()

# "with" method allows you to not close opened files
with open("./user_name.txt", "w") as f:
    f.write("I used with method")


#task part
user = input ("Input your name: ")

with open("./user_name.txt", "w") as f:
    f.write(f"{user}")



#Functions
def return_function(): 
    print("Hello from the other side")

return_function()

param_1 = "Fatima" 
param_2 = "Askerova" 

def get_fun(param1, param2):
    print(f'{param1} {param2}')

get_fun("Fatima", "Askerova")

var1= "Tech Academy" #global scope

def rtrn_prm(): #local scope 
    var1 = "Rapator"
    print(var1)

print(var1)

def lower_input_data(data):
    print(data.lower()) #you can use this with other str methods

input_1 = input("Write whatever you want: ")
lower_input_data(data = input_1)

#default arguments
def lower_input_data(data = "no data"): #add defult value
    print(data.lower()) 

input_1 = input("Write whatever you want: ")
lower_input_data()
