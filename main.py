from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
        result=dict()
        result['이름']=request.form.get('Name')
        result['학번']=request.form.get('StudentNumber')
        result['전공']=request.form.get('Major')
        result['이메일']=request.form.get('Email_id')+"@"+request.form.get('Email_addr')
        result['성별']=request.form.get("Gender")
        result['프로그래밍 언어']=",".join(request.form.getlist("PL_list"))
        return render_template('result.html',result=result)

@app.route('/result')
def delete():
    return 

if __name__ == '__main__':
    app.run(debug=True, port=8000)