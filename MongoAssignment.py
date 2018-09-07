import pymongo

client = pymongo.MongoClient()
database = client['Student']
collection = database['student']
l = []
for i in range(1,11):
        d={}
        d['Name'] = input("Enter your name")
        while(1):
            d['Marks'] = int(input("Enter your marks"))
            if 0<=d['Marks']<=100:
                break;
            else:
                print("Please enter your marks between the range(0-100)")
        l.append(d)
        print(l)
collection.insert_many(l)
data = collection.find({'Marks':{'$gt':80}})
for d in data:
    print(d)
