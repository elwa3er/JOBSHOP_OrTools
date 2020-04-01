from flask import Flask,render_template,request,url_for,redirect
from jobShop import JobShop
import json
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
        data=request.get_json()["data"]
        data=data[1:]
        data1=[]
        for d1 in data:
            j=0
            data11=[]            
            for d2 in d1:
                t=(j,int(d2))
                data11.append(t)
                j+=1
            data1.append(data11)
        lst,tps=JobShop().MinimalJobshopSat(data1)      
        return  json.dumps({"time":tps,"data":lst})








if __name__=="__main__":
    app.run(debug=True)