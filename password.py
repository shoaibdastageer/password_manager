print("Hii , Welcome to password manager \n")


def add_pass():
    while True:
        username = input("Enter your username: ").lower()
        pwrd = (input("Enter your password: "))

        if " " in username:
          print("please enter correct username without space")
          continue
          
        with open("Password.txt" , 'a')  as f:
            f.write(username + "|" + pwrd + "\n")
        print("Your password is succesfully saved\n")

        re_ask = input("DO YOU WANNA ADD ANOTHER USERNAME AND PASSWORD OR WANNA VIEW?? (yes/view): ")
        if(re_ask == "yes"):
            add_pass()
        elif(re_ask == "view"):
            view_pass()
            break

            
    
        
def view_pass():

    with open("Password.txt" , 'r') as f:
        for line in f.readlines():
             
            data = line
            user , passw = data.split("|")
            print("username: ",user ,"||","Password: ",passw)
            






view_add = input("You wanna add or view the existing one?: ")
if(view_add == "add"):
    add_pass()


elif(view_add == "view"):
    view_pass()


