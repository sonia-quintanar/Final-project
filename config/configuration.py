from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path  
from getpass import getpass
import random
from flask import Flask, jsonify
import mysql.connector

dotenv.load_dotenv()

DBURL = os.getenv("URL")

if not (DBURL):
    raise ValueError("Tienes que especificar url")

client = mysql(DBURL)
db = client.get_database()
collection = db["Dermocosmética"]