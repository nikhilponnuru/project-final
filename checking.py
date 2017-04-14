import redis

r=redis.Redis(host='localhost',port=6379)
l=[]

l=r.scan(0)
result=l[1]
value="cars"
if value in result:
    print("ok")
    print(r.lrange(value,-100,100))

