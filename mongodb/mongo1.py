from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu

#创建集合对象
myset = db.class4

#数据操作
# print(dir(myset))
# myset.insert({'name':'张铁林','King':'乾隆'})
# myset.insert([{'name':"zhangguoli",'King':'kangxi'},{'name':'chendaoming','King':'kangxi'}])
# myset.insert_many([{'name':'tangguoqiang','King':'youzheng'},{'name':'chenjianjun','King':'youzheng'}])
# myset.insert_one({'name':'zhengshaoqiu','King':'quanlong'})

#find()
# cursor = myset.find({},{'_id':0})
# print(cursor)

# for i in cursor:
# 	print(i['name'],'-------',i['King'])

# dic = myset.find_one()
# print(dic)

myset1 = db.class0
# cursor = myset1.find({'age':{'$gt':18}},{'_id':0})
# for i in cursor:
# 	print(i)

# print(cursor.next())
# print(cursor.next())

# for i in cursor.skip(1).limit(3):
# # 	print(i)
# for i in cursor.sort([('age',1),('name',-1)]):
# # 	print(i)

# cursor = myset1.find({'$or':[{'age':{'$lt':20}},{'gender':'w'}]},{'_id':0})
# for i in cursor:
# 	print(i)

# myset1.update({'name':'you'},{'$set':{'gender':'w'}},multi=True)
# dic = myset1.find({},{'_id':0})
# for i in dic:
# 	print(i)
		
myset.update({'name':'liangjia'},{'$set':{'age':20}},upsert = True)

#关闭连接
conn.close()