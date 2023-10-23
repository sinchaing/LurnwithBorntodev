print("Welcome to Tony Toy, Please sign in")
usrname = input("User Name : ")
passwrd = input("Password  : ")
if usrname == "sinchai" and passwrd == "1234" :
    print("Hi Mr.Sinchai")
    print("Please select Toy : ")
    print("1. Ipad Pro 12.9 256GB    price 48,900 THB")
    print("2. AirPod Max space gray  price 19,900 THB")
    select_item = input(">>>>>: ")
    if select_item == "1" :
        print("You select : Ipad Pro 12.9 256GB    price 48,900 THB")
        qty1 = int(input("How may device : "))
        print("Please make payment ", qty1*48900, " THB")
    elif select_item == "2" :
        print("You select : AirPod Max space gray  price 19,900 THB")
        qty2 = int(input("How may device : "))
        print("Please make payment ", qty2*19900, " THB")
else :
    print("Incorrect user or password")