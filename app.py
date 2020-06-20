from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host= "redis", port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello Docker learner! You have seen this page {0} times' . format (redis.get( 'hits' ))


def load_saved_count():
    return 1000


if __name__ == "__main__":
    redis.set('hits', load_saved_count())
    app.run(host= "0.0.0.0", debug=False)
