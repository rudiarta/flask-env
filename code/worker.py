from redis import Redis
from rq import Worker, Queue, Connection
import os

# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

conn = Redis(host=os.getenv("REDIS_HOST"),port=os.getenv("REDIS_PORT"),password=os.getenv("REDIS_PASSWORD"))
listen = ['high','default','low']

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()