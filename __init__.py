from flask import Flask, Request, Response, redirect
from config import Config
from authenticate import AuthenticateParams
from app import getProfileData
from urllib import request,parse
import json
