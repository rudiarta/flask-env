import requests
import time

def count_words_at_url(url,s):
    resp = requests.get(url)
    time.sleep(s)
    return len(resp.text.split())