# different string functions
# endswith("AIC.")

str = "i am faisal zia, i am learning python from PIAIC."
print(str.endswith("AIC."))

# capitalize

str1 = "i am faisal zia, i am learning python from PIAIC."
print(str1.capitalize())

# Replaced old,new

str2 = "i am faisal zia, i am learning python from PIAIC."
print(str2.replace("a","o"))
print(str2.replace("faisal","mohid"))

# find number or word

str3 = "i am faisal zia, i am learning python from PIAIC."
print(str3.find("r"))
print(str3.find("faisal"))

str4 = "i am faisal zia, i am learning python from PIAIC."
print(str4.count("faisal"))

# practice 

name=input("enter your name: ")
print("length of your name is", len(name))

# conditional statments

# if
age=24 
if(age >= 18):
  print("can vote")
  print("can drive")

# elif
light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
    
# else


# Nesting (if within if)
 
age=72
if(age >= 18):
    if(age >=70):
      
      print("cannot drive")
    else:
      print("can drive")
      
      # Practice nesting
      
      num = int(input("enter number: "))
      rem = num % 2
      if(rem == 0):
       print("even number")
       print("odd number")
                