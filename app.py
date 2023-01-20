from flask import Flask,render_template,request
import sqlite3 as sql
import requests

app=Flask("__name__")


@app.route("/")
def bank():
    conn=sql.connect("fund.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()

    cur.execute("select * from bank")
    data=cur.fetchall()

    return render_template("index.html",data=data)

@app.route("/fund",methods=["post","get"])
def fund():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        if id==str(1):
            l=[139619,139618,139616,139617]
        elif id==str(2):
            l=[148921,148920,148918,148919]
        elif id==str(3):
            l=[149383,149384,149382,149387]
        elif id==str(4):
            l=[148404,148406,148405,148407]
        elif id==str(5):
            l=[119354,119353,102020,102021]
    else:
        return render_template("fund.html")
    
    li=[]
    for i in l:
        url="https://api.mfapi.in/mf/"+str(i)
        resp=requests.get(url)
        temp=resp.json()
        temp2={"scheme_code":temp.get("meta").get("scheme_code"),"scheme_name":temp.get("meta").get("scheme_name"),"nav":temp.get("data")[0].get("nav")}
        li.append(temp2)
    return render_template("fund.html",data2=li)



if __name__=="__main__":
    app.run(debug=True)