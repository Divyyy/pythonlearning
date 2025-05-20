age = int(input("Enter your age: "))  # Convert input to integer

if age < 18:
    print("You are a minor")  # Corrected the message
elif age == 18:
    print("You are about to be an adult")
else:
    print("You are an adult")  # Corrected the message
