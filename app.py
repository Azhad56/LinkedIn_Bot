from flask import Flask,render_template,url_for,request
from LinkedIn_bot_v3 import LinkedInBot
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/follow_explore',methods=['POST'])
def follow_explore():
    uname = request.form['name']
    psw = request.form['pass']
    uname = str(uname)
    psw = str(psw)
    ig = LinkedInBot(uname,psw)
    ig.login()
    ig.connect_people()
    ig.closeBrowser()
if __name__ == '__main__':
	app.run(port=5000,debug=True)
