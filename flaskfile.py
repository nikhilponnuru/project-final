from flask import Flask,render_template,Session
import redis
import hashlib
from flask import request
import logging
import json
import os
import urllib
from bs4 import BeautifulSoup
import parse
import checkrediselements
#import test_pubsub

#import image_counter_test

#import poschunking


r=redis.Redis(host='localhost',port=6379)

app = Flask(__name__)
random_number=os.urandom(24)
app.secret_key =random_number
user_ip=0

@app.route('/')
def welcome():
    user_ip=request.remote_addr
    r.lpush('user_ip_addresses',user_ip)
    return render_template('login.html',ip=user_ip)




def event_stream():
    pubsub = r.pubsub()
    pubsub.subscribe('notifications')
    for message in pubsub.listen():
        print message
        yield 'data: %s\n\n' % message['data']


#these 2 endpoints from frontend




@app.route('/stream')
def stream():
    #this in frontend for displaying ad using EventSource object to call this endpoint
    return Flask.Response(event_stream(), mimetype="text/event-stream")
    #use render_template here and send event_stream()


'''
@app.route('/post', methods=['POST'])
def post():
    #this in frontend for sending blog data
    #websites which implement adsense must have action as "http://localhost:5000/post
    #from here send the content url to nltk file and from there get the keyword using import gsample.py
    data=test_pubsub.fun()
    r.publish('notifications', data)
'''




@app.route('/publisherlogin',methods=['POST'])
def login():
    print("hello baby")

    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']


        hash_object=hashlib.md5(password)
      #  password=hash_object.hexdigest()

        value = r.hget('publisher', username)



        if(value!="nil"):

            if(value==password):
                return render_template('publisher-feed.html', user=username)

            else:
                return "password didnt match"

        else:
            return "first please signup"


        r.save()





@app.route('/setprice',methods=['GET','POST'])
def setting_values_to_AD():

    if request.method=='POST':
        adcategory = request.form['Ad_category']
        setprice=request.form['setprice']

        p = r.pubsub()
        p.subscribe(adcategory)
        message=p.get_message()
        print(message)
        return "ok"

    return render_template('set_price.html')


publisher_username=''
image=''
filepath=''

@app.route('/uploadimage', methods=['GET', 'POST'])
def upload_file1():
    username="akhiul"
    print(request.form['settag'])
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.exists(username):
            os.makedirs(username)
            f.save(username+"/"+f.filename)
            r.hset(publisher_username,)
        else:
            f.save(username + "/" + f.filename)



        return render_template('publisher-feed.html')












    #r.hset(publisher_username,image,filepath)



@app.route('/sendimage',methods=['POST'])
def sendimage():
    resultimage=r.hget()


'''
@app.route('/logout/<username>')
def logout(username):

    Session.pop(username,None)

'''
@app.route('/show')
def showing():
     #print type(json.dumps(list(r.smembers('username'))))
     return json.dumps(list(r.smembers('username')))
    # return "ok"


keywords=[]
@app.route('/getdata/<url>')
def gettingwebdata(url):
    #keywords=poschunking(url)
    #final_keywords=sentimental_analysis(keywords)
    print("hurray got data {0}".format(url))
    parse(url)
    return "yes returning properly from gettingwedata"



#to display leaderboard

@app.route('/leaderboard')
def getting_leaderboard():
    data=[(100,"nik"),(20,"kame"),(30,"gauti")] #this must be the final data to be used for leadeboard
    for (score,user) in data:
        r.zadd("leadeboard",score,user)
    print(r.zrevrange("leaderboard",0,10)) #to get top 10 scorers)

    return r.zrevrange("leaderboard",0,10)













@app.route('/publisher')
def publisher():
    print("")












if __name__ == '__main__':

   app.run(threaded=True)  #for making flask to listen to multiple requests




'''

from flask import Flask


app = Flask(__name__)
#r = redis.Redis(host='localhost', port=6379)

@app.route('/hello')
def hello():
    return "hello"


if __name__== '__main__':
    app.run()
'''



