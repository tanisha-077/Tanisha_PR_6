print("====================================")
print("   PERSONAL DATA COLLECTOR")
print("====================================")
 
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
city = input("Enter your city: ")
height = float(input("Enter your height: "))
favourite_number = int(input("Enter your favourite number: "))
 
print("\n     PERSONAL INFORMATION")
print("\nName:", name)
print("Age:", age)
print("Email:",email)
print("Phone Number:", phone)
print("City:", city)
print("Height:",height)
print("Favourite Number:", favourite_number)

print("\n         DATA TYPES")
print("\nType of name:", type(name))
print("Type of age:", type(age))
print("Type of email:", type(email))
print("Type of phone:", type(phone))
print("Type of city:", type(city))
print("Type of Height:", type(height))
print("Type of favourite number:", type(favourite_number))
 
print("\n    MEMORY ADDRESSES (ID)")
print("\nID of name:", id(name))
print("ID of age:", id(age))
print("ID of email:", id(email))
print("ID of city:", id(city))
print("ID of height:", id(height))

print("\n        AGE ANALYSIS")

if age < 18:
    print("You are a Minor.")
elif age < 30:
    print("You are a Young Adult.")
elif age < 60:
    print("You are a Middle-aged Adult.")
else:
    print("You are a Senior Citizen.")
 

print("\nThank you for using Personal Data Collector!"