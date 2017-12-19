from flask import Flask
app = Flask(__name__)

@app.route('/') #will direct to homepage
def home(): #this function defines what your webpage will do
    return "Homepage here"

@app.route('/about/')
def about(): #this function defines what your webpage will do
    return "Website content goes here" #here this function return this string

if __name__=="__main__": #when you execute python script, python assigns string __main__ to the variable  __name__
    app.run(debug=True)
