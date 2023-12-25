#import the Flask class. An instance of this class will be our WSGI application.(Web Server Gateway Interface)
#import request to deal with HTTP requests
#import render_template to render a HTML file
from flask import Flask,request,render_template
#helps flask to know where to look for resources
app = Flask(__name__)
#decorator to provide additional functionality.
@app.route("/",methods=["GET","POST"])
def body_mass_index():
    name=""
    bmi=''
    if request.method=="POST" and 'username' in request.form:
        name=request.form.get('username')
    if request.method=="POST" and 'weight'  in request.form and 'height' in request.form:
        weight=float(request.form.get('weight'))
        height=float(request.form.get("height"))
        bmi=round((weight/((height/100)**2)),2)
    return render_template("index.html",name=name,bmi=bmi)
app.run()