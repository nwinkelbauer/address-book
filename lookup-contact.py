from flask import Flask, request, session, render_template
from operator import itemgetter
import csv

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload(): #path='assets/example.txt'
	error = None
	if request.method == 'POST':
		return request.form['path']
		# if not request.form['path'].endswith(('.txt', '.csv')):
		# 	error = 'Invalid username'
		# else:
		# 	# flash('You were logged in')
		# 	with open(request.form['path'], "r") as inputfile:
		# 		for row in csv.reader(inputfile):
		# 			row[0] = ''.join(e for e in row[0] if e.isalnum()).title();	#first
		# 			row[1] = ''.join(e for e in row[1] if e.isalnum()).title();	#last
		# 			#person[2] = person[2].title();			#street doesnt work w/ title bc of 2nd/3rd
		# 			row[3] = row[3].title();			#city
		# 			row[4] = row[4].upper();			#state
		# 			contacts.append(row)
		# 	# sorts the list by last name then passes list to home template		
		# 	contacts = sorted(contacts, key=itemgetter(1))
		# 	session['contacts'] = contacts;
		# 	return redirect(url_for('home'))
	#return render_template('login.html', error=error)
	pass

@app.route('/')
def home():
	contacts = []
	# adds each row as a seperate person list to the contacts list
	# parses strings in process to remove extra characters/formats
	with open('assets/example.txt', "r") as inputfile:
		for row in csv.reader(inputfile):
			row[0] = ''.join(e for e in row[0] if e.isalnum()).title();	#first
			row[1] = ''.join(e for e in row[1] if e.isalnum()).title();	#last
			#person[2] = person[2].title();			#street doesnt work w/ title bc of 2nd/3rd
			row[3] = row[3].title();			#city
			row[4] = row[4].upper();			#state
			contacts.append(row)
	# sorts the list by last name then passes list to home template		
	contacts = sorted(contacts, key=itemgetter(1))
	return render_template('home.html', contacts=contacts)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload(path='assets/example.txt'):
#     # do something to send email
#     pass

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)