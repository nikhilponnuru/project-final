

from flask import Flask,render_template
import test_pubsub

app = Flask(__name__)

'''
def event_stream():
    pubsub = red.pubsub()
    pubsub.subscribe('notifications')
    for message in pubsub.listen():
        print message
        yield 'data: %s\n\n' % message['data']


@app.route('/post', methods=['POST'])
def post():
    data=test_pubsub.fun()
    red.publish('notifications', data)
    return flask.redirect('/')


@app.route('/stream')
def stream():
    return flask.Response(event_stream(), mimetype="text/event-stream")
'''
'''

@app.route('/data.csv')
def data():
   return render_template('data.csv')


@app.route('/')
def index():


    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)

'''

import nltk
nltk.download('all')

