from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/',methods = ['GET','POST'])
def root():
    name = ''
    idy = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        idy = request.form.get('idy')
    return render_template("index.html",name=name,idy=idy)

@app.route('/bmi',methods = ['GET','POST'])
def bmi():
    weight = 0
    height = 0
    bmi = None
    if request.method == 'POST' and 'height' in request.form:
        weight = float(request.form.get('weight',0))
        height = float(request.form.get('height',0))
        bmi = weight/((height/100) ** 2)
        bmi = int(bmi*10)/10
    return render_template("bmi.html",weight=weight,height=height,bmi=bmi)

    
app.run()
