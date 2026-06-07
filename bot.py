while True:
    try:
        age=int(input("What is your age ? \n"))
    except ValueError:
        print("Invalid Input")
        continue
    name=input("Enter your name ? \n")
        
    if age >= 18:           
         print(f"{name} is eligible to vote in india!")
         continue
    else:
         print(f"{name} is not eligible to vote in india!")
         continue
    