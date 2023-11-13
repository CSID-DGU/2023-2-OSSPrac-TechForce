from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['university'] = request.form.get('university')
        result['Gender'] = request.form.get('gender')
        result['Major'] = request.form.get('major')
        result['Email'] = request.form.get('email') + request.form.get('email-ad')
        result['Programming Languages']=request.form.get('option')
        return render_template('result.html',result=result)


if __name__ =='__main__':
    app.run(debug=True)