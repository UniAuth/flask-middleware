from flask import Flask, Request, Response, redirect
from .interface.config import Config
from .interface.authenticate import AuthenticateParams
from .minions.minions import getProfileData

class UniAuth :
    configs = []
    def __init__(self,configs : list):
        self.config = configs


    def __fillDefaults(self,config : Config):
        if(not(config.name)):
            raise Exception("name and url required")

        if(not(config.processor)):
            #  ToDo : function should also take profile parameter
           config.processor(next) 


        # define default endpoints
        if(not(config.endpoint)):
            config.endpoint = {
                'auth': 'account/o/login',
                'profile': 'account/o/access',
            }

    def __getConfigByName(self,name:str):
         item =  list(filter((lambda x : x['name'] == name ),self.config))
         print(item,"hehehe")
         if (len(item) == 0) :
             raise Exception(f'Config named {name} was not found')
         elif(len(item)>1):
             raise Exception(f'Configs with duplicate name :: {name} found')
         else:
             return item[0]

    def authenticate(self,name: str):
        config = self.__getConfigByName(name)
        loginUrl = f'{self.config[0]["url"]}/{self.config[0]["endpoint"]["auth"]}?client_id={self.config[0]["clientId"]}&redirect_uri={self.config[0]["redirectUri"]}'    
        print(loginUrl)
        return loginUrl       

    
    def callback(self,name: str,function):
        Config = self.__getConfigByName(name)
        async def function(req:Request, res:Response):
            accessToken = req.args.get('access_token')
            profileDetails = await getProfileData(config,accessToken)
            await config.processor(profileDetails)
        return function(Request,Response)



