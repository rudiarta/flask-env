from redis import Redis
from rq import Queue
import os

# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

class Helpers():
    
    def __init__(self):
        pass

    def initQueue(priority):
        return Queue(priority,connection=Redis(os.getenv("REDIS_HOST"),os.getenv("REDIS_PORT"),password=os.getenv("REDIS_PASSWORD")))
    