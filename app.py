from flask import Flask, render_template, request, session, redirect
 # 내가 만든 id pw 체크 함수
import db

app = Flask(__name__)
app.secret_key = b'aaa!111/'

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/korean')
def korean():
    return render_template('korean.html')

@app.route('/chinese')
def chinese():
    return render_template('chinese.html')

@app.route('/japan')
def japan():
    return render_template('japan.html')

@app.route('/flour')
def flour():
    return render_template('flour.html')

@app.route('/chicken')
def chicken():
    return render_template('chicken.html')

@app.route('/hamburger')
def hamburger():
    return render_template('hamburger.html')

@app.route('/ladder')
def ladder():
    return render_template('ladder.html')

#if __name__ == '__main__':
#    app.run()