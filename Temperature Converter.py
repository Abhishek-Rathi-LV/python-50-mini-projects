def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32
def fahrenheit_to_celsius(temp):
    return(temp - 32) *5/9
def Celsius_to_Kelvin(temp):
    return  temp + 273.15
def Kelvin_to_Celsius(temp):
    return  temp - 273.15
def Fahrenheit_to_Kelvin(temp):
    return (temp - 32) * 5/9 + 273.15
def Kelvin_to_Fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32
while True:
    print(" ===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius \n 3. Celsius to Kelvin \n 4. Kelvin to Celsius \n 5. Fahrenheit to Kelvin \n 6. Kelvin to Fahrenheit \n 7. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        temp=float(input("Enter temperature in Celsius"))
        res=celsius_to_fahrenheit(temp)
        print(temp , "Celcius =",res,"Fahrenheit")
    elif choice==2:
        temp=float(input("Enter temperature in Farheneit"))
        res=fahrenheit_to_celsius(temp)
        print(temp , "Fahrenheit =",res,"Celcius")
    elif choice==3:
        temp=float(input("Enter temperature in Celsius"))
        res=Celsius_to_Kelvin(temp)
        print(temp , "Celcius =",res,"kelvin")
    elif choice==4:
        temp=float(input("Enter temperature in kelvin"))
        res=Kelvin_to_Celsius(temp)
        print(temp , "kelvin =",res,"Celcius")
    elif choice==5:
        temp=float(input("Enter temperature in Farheneit"))
        res=Fahrenheit_to_Kelvin(temp)
        print(temp , "Fahrenheit =",res,"kelvin")
    elif choice==6:
        temp=float(input("Enter temperature in kelvin"))
        res=Kelvin_to_Fahrenheit(temp)
        print(temp , "kelvin =",res,"farenhie")
    elif choice==7:
        print("Program is extting ")
        break
    else:
        print("Wrong Input try again ")


         
