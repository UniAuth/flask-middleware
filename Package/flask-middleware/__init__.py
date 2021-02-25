from flask import Flask, Request, Response, redirect
from config import Config
from authenticate import AuthenticateParams
from minions import getProfileData
from urllib import request,parse
import json
