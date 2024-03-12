import sqlite3
import os

url = os.getcwd() + "/app/database/foo.db"
conn = sqlite3.connect(url)