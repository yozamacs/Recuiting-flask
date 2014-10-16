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
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
	if request.method == "GET":
	    	for f in os.listdir("/Users/maryumstyles/example/CSVs"):
			if f.endswith(".csv"):
				schoolList.append(f)
	   	return render_template('button.html',schoolList =schoolList)
   	else:
   		app_lulu.checkboxValues = request.form
		if len(app_lulu.checkboxValues)==0:
			outcome = 'no checkboxes checked'
			return render_template('submit.html', outcome=outcome)
		else:
   			for key in app_lulu.checkboxValues:
   				schoolName = key.strip('\'')
				if(subprocess.call(['java', '-jar', 'tw-recruiting.jar', '/Users/maryumstyles/example/CSVs/'+schoolName])!=0):
					outcome = 'failure'
					#output = subprocess.check_output(['ls', '-1']) wanted to get error log....do that in the future
					return render_template('submit.html', outcome=outcome)
			outcome = 'success'
			return render_template('submit.html', outcome=outcome)


if __name__ == '__main__':
    app_lulu.run(debug=True)
