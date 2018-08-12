from flask import Flask, request
from firebase import firebase

app = Flask(__name__)
thread = None

firebase = firebase.FirebaseApplication('https://smartcanine-c15e7.firebaseio.com/',None)

@app.route("/", methods = ['POST'])
def backgound_thread():
	if request.method == 'POST':
		user = request.form['test']
		print(user)
		firebase.patch('userlog', {'test': user})

	return "Hello"

if __name__ == "__main__":
	app.run(host='192.168.43.14', port=4000, debug=True)
