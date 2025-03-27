def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("OPERATIONS:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modular Division")
        
        user_input=input("Enter your choice:")
        num = ['1','2','3','4','5']
        
        if user_input in num:
            if user_input == '1':
                print("Answer:",num1+num2)
            elif user_input == '2':
                print("Answer:",num1-num2)
            elif user_input == '3':
                print("Answer:",num1*num2)
            elif user_input == '4':
                if num2 != 0:
                    print("Answer:",num1/num2)
                else:
                    print("Error! Division by zero is not allowed.")
            elif user_input == '5':
                if num2 != 0:
                    print("Answer:",num1%num2)
                else:
                    print("Error! Division by zero is not allowed.")
        else:
                print("Invalid choice. Please choose a valid operation.")
    except ValueError:
        print("Please enter valid numbers.")
        
if __name__=="__main__":
    calculator()
        
             
                    
                    
                    
                    
                    
                    
                
        
    