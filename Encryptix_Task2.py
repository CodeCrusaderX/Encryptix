num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number:"))
print("First Number entered is ",num1)
print("First Number entered is ",num2)
def Calculator():
    while True:
        try:
            operation = int(input("Enter your choice: \n1-Add\n2-Subtract\n3-Multiplication\n4-Division\n5-Exit\n"))
            if operation == 1:
                sum = num1+num2
                print(f"Both numbers have been successfully added. Their sum is ",sum)

            elif operation == 2:
                diff = num1-num2
                print(f"Both numbers have been successfully subtracted. Their difference is ",diff)

            elif operation == 3:
                product = num1*num2
                print(f"Both numbers have been successfully multiplied. Their product is ",product)

            elif operation == 4:
               quotient = num1/num2
               print(f"Both numbers have been successfully divided. Their quotient is ",quotient)
            elif operation == 5:
                print("To Do List is Closed!\nThank you for using it :)")
            
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")
Calculator()