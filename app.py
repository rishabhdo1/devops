from flask import Flask,request ,render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.test
collection = db["users"]



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form_data = dict(request.form) # Convert ImmutableMultiDict to a regular dictionary
    result = collection.insert_one(form_data)
    return f"✅ User inserted with ID: {result.inserted_id}"

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)  # Convert cursor to list to print all items

    for item in data:
        print(item)
        
        del item['_id']  # Remove the MongoDB-generated _id field for cleaner output
    
    data = {
        'data': data
    }
    return data

    
   

if __name__ == '__main__':
    app.run(debug=True) #debug=True means it will auto-reload on code changes
