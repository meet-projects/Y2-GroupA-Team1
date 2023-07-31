from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templet', static_folder='static')
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

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/post_question", methods=["POST"])
def post_question():
    question = request.form["question"]
    
    # Save the question to Firebase Firestore
    question=db.child("qna").push({"question": question, "answer": "",'UID':""})
    # print(question['name'])
    UID=question['name']
    db.child("qna").child(UID).update({'UID':UID})
    return redirect("/qna")


# def reply():
@app.route("/reply", methods=["POST"])
def reply():
    print('hi')
    reply_text = request.form["reply"]
    question_id = request.form["question_id"]
    print(question_id)

    # Create a new "reply" entry for the question in Firebase Realtime Database
    print(db.child('qna').child(question_id).get().val())
    db.child("qna").child(question_id).update({"answer": reply_text})
    
    return redirect("/qna")
@app.route("/qna", methods=["GET", "POST"])
def qna():
    entries = []
    # Retrieve all questions from Firebase Firestore
    questions_ref = db.child("qna").get()
    for question in questions_ref:
        entries.append(question.val())
    return render_template("qna.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
