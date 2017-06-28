
go = True
while go:

    print("Choose an operation.")   
    print("1.Add")
    print("2.Subtract")
    print("3.Exit")

    choice=input("Enter number for operation: ")

    num1=input("enter value 1: ")
    num2=input("enter value 2: ")


    if choice == '1':
        sum1 = num1 + num2
        print ("The sum of", num1,"+",num2,"=",sum1)
        input("press any enter to continue...")
        

    elif choice == '2':

        sum1 = num1 - num2
        print ("The value of", num1,"-",num2,"=",sum1)
        input("press any enter to continue...")
    

    elif choice == '3':
        print("Cya!")
        go = False
    
    else:
        print("invalid choice!")
        
  
