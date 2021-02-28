from src.interface.config import Config
from urllib import request,parse
import json


async def getProfileData(config: Config, accessToken: str):
    try: accessToken
    except NameError: print("access_token undefined")

    url = f"{config.url}/{config.endpoint['profile']}"
    
    body = await parse.urlencode({
        "clientId" : config.clientId,
        "clientSecret" : config.clientSecret,
        "accessToken" : accessToken
    }).encode()

    req =await request.Request(url = url,data = body)
    req.add_header('Content-Type', 'application/json')
    response = await request.urlopen(req)
    data = json.dumps(response)    
    return data

    