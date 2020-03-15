from pymongo import MongoClient
conn = MongoClient('localhost',27017)
db= conn.stu
myset = db.class0

#index 

# index = myset.ensure_index('name')
# print(index)
# index = myset.ensure_index([('age',-1)])

# for i in myset.list_indexes():
# 	print(i)

# myset.drop_indexes()

# myset.drop_index('name_1')
# myset.ensure_index([('name',1),('age',-1)])

# myset.ensure_index('name' ,name = 'MyIndex',unique = True)

myset.ensure_index('age',sparse = True)

conn.close()
		