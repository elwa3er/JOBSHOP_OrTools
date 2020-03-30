from flask import Flask,render_template,request,url_for,redirect
from jobShop import JobShop
app=Flask(__name__)




@app.route("/jobshop/home",methods=["GET"])
def home():
    return render_template("index.html")
@app.route('/', methods=["GET"])
def defaultRoot():
    return redirect(url_for("home"))
@app.route("/jobshop/manual", methods=["GET","POST"])
def manual():
    if request.method=="GET":
        return render_template("grid.html")
    else:
        return "post"








if __name__=="__main__":
    app.run(debug=True)