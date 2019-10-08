from redis import Redis
from rq import Queue
from logic.Article import count_words_at_url

q = Queue(connection=Redis("7.7.7.4",6379,password=''))
a = count_words_at_url
result = q.enqueue(a, 'http://nvie.coms',2)
print(result)