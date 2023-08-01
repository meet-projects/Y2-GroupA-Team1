from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templets', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key '

firebaseConfig = {
  "apiKey": "AIzaSyAMng7Xrimcf8DdC-oeSD1iKhHa2aFw5nM",
  "authDomain": "questions-and-answers-145b9.firebaseapp.com",
  "projectId": "questions-and-answers-145b9",
  "storageBucket": "questions-and-answers-145b9.appspot.com",
  "messagingSenderId": "1041152034637",
  "appId": "1:1041152034637:web:c4d0b370d55a9dbd3f1904",
  "measurementId": "G-6J5HH8BP8Y",
  "databaseURL":'https://questions-and-answers-145b9-default-rtdb.europe-west1.firebasedatabase.app/'
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db =firebase.database()
#Code goes below here 

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/Q&A',methods=['GET','POST'])
def questionandanswer():
    if request.method=='POST':
        question = request.form["question"]
        # Save the question to Firebase Firestore
        db.collection("qna").add({"question": question, "answer": ""})
        return redirect("/qna")
    else:
        return render_template('Q&A.html')

#Code goes above here

@app.route('/apply')
def apply():
    return render_template('apply.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
