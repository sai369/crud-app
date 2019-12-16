import pymongo
import json
from flask import Flask

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydata"]

mycol = mydb["Employees"]

print("select your operation:\n1.Create \n2.Read \n3.Update \n4.Delete")

operation=input("select your operation:")

@app.route('/')
def hello_world():
   return "Hello World"



@app.route('/create')
def create():
    create_data = []
    mydict = [{ "name": "Husain", "address": "Mumbai" },
              {"name": "Ajay", "address": "Hyderabad"},
              {"name": "Arun", "address": "Hyderabad"}
              ]


    create_res = mycol.insert_many(mydict)
    create_data.append(mydict)
    return ' '.join([str(elem) for elem in create_data])

    print("=======response---------", create_res)

    for x in mycol.find():
        print(x)

    read_data = []

    return "Data Insterted successfully"


@app.route('/read')
def read():
    read_data = []
    for x in mycol.find():
        del x['_id']
        read_data.append(x)

    return ' '.join([str(elem) for elem in read_data])

@app.route('/update')
def update():
    # update_data = []
    update_res = mycol.update_one({"Name": "Ajay"}, {"$set": {"Name": "Anil"}})
    #update_data.append(update_res)
    #return update_res
    #for x in mycol. update_res.find():
    # del  update_res['_id']
    # update_data.append(update_res)
    # return ' '.join([str(elem) for elem in update_data])

    update_data= []
    for x in mycol.find():
        del x['_id']
        update_data.append(x)

    return ' '.join([str(elem) for elem in update_data])



    # update_data = []
    # for x in update_res.find():
    #     del x['_id']
    #     update_data.append(x)
    #
    # return ' '.join([str(elem) for elem in update_data])
    #


    #return "Data Updated successfully"

@app.route('/delete')
def delete():
    #delete_data = []
    delete_res = mycol.delete_one({"name": "Arun"})
    #delete_data.append(delete_res)

    #return ' '.join([str(elem) for elem in delete_res])

    delete_data = []
    for x in mycol.find():
        del x['_id']
        delete_data.append(x)

    return ' '.join([str(elem) for elem in delete_data])

    #return delete_res

    #return "Data Deleted successfully"

def perform_action(operation):
    switcher = {
        '1': create,
        '2': read,
        '3': update,
        '4': delete
    }

    data_action =  switcher.get(operation)

    return data_action()


if __name__ == '__main__':
    perform_action(operation)
    app.run()


D:\Practice\crud flask.py