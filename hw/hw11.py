#python exeption 

try:
    f = open('test_txt') 
      
except FileNotFoundError as e: #first put more specific exeption
    print(e)

except Exception as e :
     print('Error!')

else:
    print(f.read())
    f.close()

finally: #always runs 
    print("Executing Finally...")