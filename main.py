from flask import Flask,render_template,request

app=Flask(__name__)

rows = [] # 딕셔너리 데이터가 담긴 리스트

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result',methods=['GET','POST'])
def result():
    global rows
    if request.method=='POST':
        result=dict()
        result['이름']=request.form.get('Name')
        result['학번']=request.form.get('StudentNumber')
        result['전공']=request.form.get('Major')
        result['이메일']=request.form.get('Email_id')+"@"+request.form.get('Email_addr')
        result['성별']=request.form.get("Gender")
        result['프로그래밍 언어']=",".join(request.form.getlist("PL_list"))
        rows.append(result)
        return render_template('result.html',rows=rows)
    else:
        if not rows:
            rows = [{}]
        return render_template('result.html',rows=rows)
    
#add 기능 추가
@app.route('/add', methods=['GET', 'POST']) 
def add():
    global rows
    if request.method == 'POST':        
        if 'add_row' in request.form:
            rows.append({})
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
