from __future__ import print_function
from flask import Flask, render_template, request, redirect
import os,subprocess
app_lulu = Flask(__name__)
app_lulu.checkboxValues = []

@app_lulu.route('/', methods=['GET'])
def test():
	return redirect('/home')

@app_lulu.route('/home', methods=['GET','POST'])
def home():
	schoolList = []
	if request.method == "GET":
	    	for f in os.listdir("CSVs"):
			if f.endswith(".csv"):
				schoolList.append(f)
	   	return render_template('button.html',schoolList =schoolList)
   	else:
   		app_lulu.checkboxValues = request.form
		if len(app_lulu.checkboxValues)==0:
			outcome = 'no checkboxes checked'
		else:
   			for key in app_lulu.checkboxValues:
   				schoolName = key.strip('\'')
				if(subprocess.call(['java', '-jar', 'tw-recruiting.jar', 'CSVs/'+schoolName])!=0):
					outcome = 'failure'
					#output = subprocess.check_output(['ls', '-1']) wanted to get error log....do that in the future
				else:
					outcome = 'success'
		return render_template('submit.html', outcome=outcome)


if __name__ == '__main__':
    app_lulu.run(debug=True)
