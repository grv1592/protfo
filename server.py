from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def save_data(data):
	with open('C:/Users/GauravKumar/Desktop/python programs/Web Server/database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write('\n{}, {}, {}'.format(email ,subject ,message))


def write_data_csv(data):
	with open('C:/Users/GauravKumar/Desktop/python programs/Web Server/database.csv',newline = '', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email ,subject ,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
		    data = request.form.to_dict()
		    print(data)
		    write_data_csv(data)
		except: 
			return 'did not save to database'
		return redirect('./form_submitted.html')
	else:
		return "Something went wrong"
    

