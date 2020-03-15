from pymongo import MongoClient
from random import randint

conn = MongoClient('localhost',27017)
# db= conn.stu
# myset = db.class4

# p = [{'$group':{'_id':'$King','count':{'$sum':1}}},{'$match':{'count':{'$gt':1}}}]

# cursor = myset.aggregate(p)

# for i in  cursor:
# 	print(i)

db = conn.grade
myset = db.class0
# cursor = myset.find()
# for i in cursor:
# 	myset.update({'_id':i['_id']},{'$set':{'score':{'chinese':randint(60,100),\
# 		'math':randint(60,100),'english':randint(60,100)}}})

# cursor = myset.find({},{'_id':0})
# for i in cursor:
# 	print(i)

# cursor = myset.aggregate([{'$group':{'_id':'$sex','num':{'$sum':1}}}])
# cursor = myset.aggregate([{'$match':{'sex':'m'}},\
# 	{'$project':{'_id':0,'name':1,'sex':1,'score.chinese':1}}])

cursor = myset.aggregate([{'$match':{'sex':'w'}},{'$sort':{'score.english':-1}}])


for i in cursor:
	print(i)




conn.close()
