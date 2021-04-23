from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getdata', methods=['POST','GET'])
def getdata():

    df = pd.read_csv('sheets/sheet1.csv')

    if request.method == 'POST':

        f_name = request.form.get("fname")
        l_name = request.form.get("lname")
        age = int(float(request.form.get("age")))

        if f_name!=None:

            df = df.append({'id':df.id.values[-1] + 1,'fname':f_name,'lname':l_name,'age':age},ignore_index=True)

            df.to_csv('sheets/sheet1.csv',index=False)

    data = df.to_dict(orient='records')


    return render_template('output.html',df = df,data = data)


@app.route('/uploaddata')
def uploaddata():

    return render_template('input.html')


# @app.route('/downloadcsv')
# def downloaddata():

if __name__=='__main__':
  app.run(debug=True)