from flask import Flask, render_template, url_for,request,redirect
from flask_pymongo import pymongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://new:newpassword123@cluster0.pw6li.mongodb.net/blog?retryWrites=true&w=majority")
client2 = pymongo.MongoClient("mongodb+srv://new:newpassword123@cluster0.pw6li.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database('Test2')
db2 = client2.get_database('test')
@app.route('/')
@app.route('/index')
def index():
    di = {}
    i=0
    cursor = db2.new
    for document in cursor.find():
        di[i] = document
        i +=1
    print(di)
    return render_template('index.html', title='Home',data=di)

@app.route('/result')
def res():
    x = []
    cursor = db.posts
    for document in cursor.find():
        x.append(document)
    print(x)
    return render_template('new.html',thing = x)

#no
@app.route('/', methods=['POST'])
def my_form_post():
    cursor = db2.new
    data = request.form
    author = request.form['comment_author']
    email = request.form['email']
    comment = request.form['comment']
    article_id = request.form['comment_post_ID']
    insDoc = {
        'author' : author,
        'time' : datetime.now(),
        'email' : email,
        'comment': comment,
        'article_id':article_id
    }
    print(data)
    x = cursor.insert_one(insDoc)
    print(x)
    return render_template('intermediate_comment.html', data=insDoc)


if __name__ == "__main__":
    app.run(debug=True)
