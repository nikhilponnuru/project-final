from flask import Flask,url_for,redirect

import redis

r=redis.Redis(host='localhost',port=6379)
app = Flask(__name__)

r.set('image1', 1)
r.set('image2',1)
r.set('image3',1)
r.set('image5',1)
r.set('image4',1)

imagename=''
@app.route('/<image_name>')
def f1(image_name):
    global imagename
    imagename= image_name
    return redirect('https://www.tutorialspoint.com/flask/flask_redirect_and_errors.htm')


@app.route('/<image_name>/image')
def f2():
    image = imagename

    r.incr(image)
    print(r.get(image))
    return r.get(image)



if __name__ == '__main__':

   app.run(threaded=True)  #for making flask to listen to multiple requests




