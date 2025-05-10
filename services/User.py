from utils.helpers import load_data,save_data,logger
from utils.decorators import verify_password,hash_password


class Users:
    
    User_json = "data/Users.json"

    def __init__(self,Name,Username,Email,Password,Role):
        self.Name = Name 
        self.Username = Username 
        self.Email = Email  
        self.Password = hash_password(Password) 
        self.Role = Role 

    def view_profile(self):
        print(f"Name of the user : {self.Name}")
        print(f"Name of the username : {self.Username}")
        print(f"Name of the email : {self.Email}")
        print(f"Name of the Role : {self.Role}") 

    def to_dict(self):
        return vars(self)

    def create_user(self):
        data = load_data(self.User_json)
        data.append(self.to_dict())
        save_data(self.User_json,data)
        logger.debug(f"User Succesfully created for {self.Username}")
        return data  
    
    @staticmethod
    def login_user(username,password):
        data = load_data(Users.User_json)
        for i in data:
            if (i.get('Username') == username) and (verify_password(password,i.get('Password'))):
                logger.debug(f" User: {i.get('Username')} succesfully logged in.")
                return "User logged in"
        logger.error("User Credentials not found in data")
        return "User not listed in data"

    @staticmethod
    def delete_user(username,email):
        data = load_data(Users.User_json)
        for i in data:
            if i.get('Username') == username and i.get('Email')==email:
                data.remove(i)
                save_data(Users.User_json,data)
                logger.debug(f"Deleted user {i.get('Username')}")
                return "User Deleted Succesfully"
        logger.error("User Credentials not found in data")
        return "User not listed in data"
            
    @staticmethod
    def list_all_users():
        data = load_data(Users.User_json)
        for i in data:
            print(f"Name : \033[92m{i.get('Name')}\033[0m , Role : \033[92m{i.get('Role')}\033[0m ")
        logger.debug("Succesfully returned list all users")
        return "Succesfully listed all Users"    




            



        




