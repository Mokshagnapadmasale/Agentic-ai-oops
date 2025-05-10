from services.User import Users 

def show_admin_menu():
        
        print("1 : Create User")
        print("2 : Login User")
        print("3 : Delete User")
        print("4 : List all Users")
        print("")
        print("--------------------------------------------------------")
        print("")

def show_user_menu():
        
        print("1 : Login User")
        print("")
        print("--------------------------------------------------------")
        print("")
     
def main():
    while True:
        print("Welcome to Role Baseed Application")
        print("")
    
        Role = str(input('Enter Role admin/Users :  ')).strip().lower()
    
        if Role == "admin":
            
            show_admin_menu()
            choice = int(input("Enter your choice :  "))

            if choice == 1:
                Name = str(input("Enter your Name :  "))
                Username = str(input("Enter your UserName :  "))
                Email = str(input("Enter your Email [ex:name@gmail.com] :  "))
                Password = str(input("Enter your Password :  "))
                Role = str(input("Enter your Role :  "))
                obj = Users(Name,Username,Email,Password,Role)
                obj.create_user()
                print("")
                obj.view_profile()
    
            elif choice == 2:
                Username = str(input("Enter your UserName :  "))
                Password = str(input("Enter your Password :  "))

                result = Users.login_user(Username,Password)
                print(result)

            elif choice == 3:
                Username = str(input("Enter your UserName :  "))
                Email = str(input("Enter your Email [ex:name@gmail.com] :  ")) 

                result = Users.delete_user(Username,Email)
                print(result)

            elif choice == 4:
                Users.list_all_users()    

    
            print("")            

        elif Role == "user":
            show_user_menu()
            choice = int(input("Enter your choice :  "))
            if choice == 1:
                Username = str(input("Enter your UserName :  "))
                Password = str(input("Enter your Password :  "))
                result = Users.login_user(Username,Password)
                print(result)
                print("")
        cond = str(input("Enter Yes/NO to continue or Exit from Application :  ")).strip().lower()
        if cond != "yes":
            break    
         
if __name__ == "__main__":
    main()
   


