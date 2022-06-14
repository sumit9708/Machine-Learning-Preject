from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route("/")
def hi():
    return "This is my code for deployment"

if __name__=="__main__":
    app.run(debug=True)