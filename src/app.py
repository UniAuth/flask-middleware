from flask import Flask, request, Response, redirect
from interface.config import Config
from interface.authenticate import AuthenticateParams

class UniAuth :
    configs = Config
    def __init__(self):
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

    def __getConfigByName(self,name:str,config : Config):
         item =  filter((lambda x : config.name == name ),config)

         if (len(item) == 0) :
             raise Exception(f'Config named {name} was not found')
         elif(len(item)>1):
             raise Exception(f'Configs with duplicate name :: {name} found')
         else:
             return item[0]

    def authenticate(self,name: str):
        config = self.__getConfigByName(name)

        def function(req = request, res = Response, next = next()):
            loginUrl = f'{config.url}/{config.endpoint.auth}?client_id={config.clientId}&redirect_uri={config.redirectUri}'    
            redirect(loginUrl)
            next()
        return function()


