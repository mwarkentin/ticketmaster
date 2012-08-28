import os
import urlparse

from redis import StrictRedis

from flask import Flask, jsonify
app = Flask(__name__)

HEROKU = 'HEROKU' in os.environ

if HEROKU:
    urlparse.uses_netloc.append('redis')
    redis_url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
    redis = StrictRedis(
        host=redis_url.hostname,
        port=redis_url.port,
        password=redis_url.password
    )
else:
    redis = StrictRedis()


@app.route('/')
def list():
    """List ticket tapes"""
    ticket_tapes = []
    for k in redis.keys():
        ticket_tapes.append({k: int(redis.get(k))})
    return jsonify(ticket_tapes=ticket_tapes)


@app.route('/<ticket_tape>/', methods=['POST'])
def request_ticket(ticket_tape):
    """Return a unique id for :ticket_tape"""
    id = int(redis.incr(ticket_tape))
    return jsonify(ticket_tape=ticket_tape, id=id)

if __name__ == '__main__':
    if not HEROKU:
        app.debug = True

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
