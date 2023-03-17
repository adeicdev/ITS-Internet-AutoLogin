# PUT YOUR ITS USER ACCOUNT HERE!
ITS_NRP      = "" # str
ITS_PASSWORD = "" # str

# Wrapper for User Configuration
class UserParameters:
    def __init__(self) -> None:

        if len(ITS_NRP) == 0:
            print("Please Configure your ITS NRP in 'Account.py'")
        
        if len(ITS_PASSWORD) == 0:
            print("Please Configure your ITS Password in 'Account.py'")
        
        self.username = str(ITS_NRP)
        self.password = str(ITS_PASSWORD)
    
    def __str__(self) -> str:
        readacted_password     = '*' * len(self.password)
        readacted_password[0]  = self.password[0]
        readacted_password[-1] = self.password[-1]
        return f"Username : {self.username}; Password : {readacted_password}"
        