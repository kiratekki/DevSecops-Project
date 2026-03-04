from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username == 'admin' and password == 'password123': 
			return redirect(url_for('home')) 
		else: 
			return(" Credentials mismatch ")
	return''' 
    		<form method="POST" action="/login">
    		<input type="text" name="username" placeholder="Username"><br>
    		<input type="password" name="password" placeholder="Password"><br>
    		<input type="submit" value="Login">
		</form>
		'''
@app.route('/home', methods=['GET']) 
def home(): 
   return '''
      <H1> "Welcome to the Homepage" </H1> '''

if __name__ == '__main__':
	app.run(debug=True)
