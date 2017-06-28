print("Hello, world! This is my calculator.")#displays hello world!

while True: #loopz
    try:
        def add(a,b): #define variables
            return a + b
        def minus(a,b):
            return a - b
        def times(a,b):
            return a * b
        def divide(a,b):
            return a / b


        print ("choose an operation:")

        print (" 1.add ")
        print (" 2. minus")
        print (" 3. times")
        print ( "4. divide")

        c = int(input("1/2/3/4: ")) #choice function

        a = int(input("key in your first value: ")) #give values
        b = int(input("key in your second value"))

        if c == 1:
            print (a, "+", b, "=", add(a,b))
            while True:#loop
                print("More?")
                response = input("Type 'Y' for yes or 'N' for no. \n")
                if response == ('y' or 'Y'):
                    stop = False
                    break
                elif response == ('n' or 'N'):
                    stop = True
                    break
                else:
                    continue
            if stop:
                break

        elif c == 2:
            print (a, "-", b, "=", minus(a,b))
            while True:#loop
                print("More?")
                response = input("Type 'Y' for yes or 'N' for no. \n")
                if response == ('y' or 'Y'):
                    stop = False
                    break
                elif response == ('n' or 'N'):
                    stop = True
                    break
                else:
                    continue
            if stop:
                break

        elif c == 3:
            print (a, "*", b, "=", times(a,b))
            while True:#loop
                print("More?")
                response = input("Type 'Y' for yes or 'N' for no. \n")
                if response == ('y' or 'Y'):
                    stop = False
                    break
                elif response == ('n' or 'N'):
                    stop = True
                    break
                else:
                    continue
            if stop:
                break

        elif c == 4:
            print (a, "/", b, "=", divide(a,b))
            while True:#loop
                print("More?")
                response = input("Type 'Y' for yes or 'N' for no. \n")
                if response == ('y' or 'Y'):
                    stop = False
                    break
                elif response == ('n' or 'N'):
                    stop = True
                    break
                else:
                    continue
            if stop:
                break

        else:
            print ( "the function does not exist or you keyed in an invalid option")
            while True:#loop
                print("Do you wish to try again?")
                response = input("Type 'Y' for yes or 'N' for no. \n")
                if response == ('y' or 'Y'):
                    stop = False
                    break
                elif response == ('n' or 'N'):
                    stop = True
                    break
                else:
                    continue
            if stop:
                break

    except ValueError:
        print("Invalid Input brotha")

print("O well... see you next time.")
input("press enter to continue...")
