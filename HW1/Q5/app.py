from flask import Flask, render_template, request, json, jsonify 

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('hello.html')

@app.route('/regis_process', methods=['POST', 'GET'])
def regis_process():

	email = request.form['email']
	pwd = request.form['password']
	
	num = upper = False

	print(email,pwd)

	for c in pwd:
		if c.isdigit(): 
			num = True
		elif c.isupper(): 
			upper = True
		
		if num and upper and len(pwd) >= 8:
			return jsonify({"status" : True,"email_data": email, "password_data": pwd})
		
	erro_msg = []

	if len(pwd) < 8:
		erro_msg.append(1)
	if num == False:
		erro_msg.append(2)
	if upper == False:
		erro_msg.append(3)


	return jsonify({"status" : False, "email_data": email, "password_data": erro_msg})


@app.route('/signup')
def signup():
	return render_template('signup.html')


if __name__=="__main__":
	app.run()