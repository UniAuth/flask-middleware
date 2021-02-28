class configInterface:
     def __init__(self):
        self.name = str
        self.url = str
        self.clientId = str
        self.clientSecret = str
        self.redirectUri = str
   

#    option method to set custom endpoints if using modified server
    
        self.endpoint = {
            "auth" : str,
            "profile" : str
        }

     def processor(self,profile): None
Config = configInterface()  