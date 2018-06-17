from flask import Flask
from flask import render_template
from flask import request
from threading import Thread
sorted = False


def sortNumber(num, l):
	global sorted
	for i in range(l, len(num)-1, 2):
		if num[i] > num[i+1] :
			num[i],num[i+1] = num[i+1],num[i]
			sorted = False
		elif num[i] == num[i+1]:
			i+= 2
def sort(num):
	global sorted
	sorted = False
	while not sorted:
		sorted=True
		t = Thread(target=sortNumber(num,0))
		t1 = Thread(target=sortNumber(num,1))
		t.start()
		t1.start()
		t.join()
		t1.join()
	return num






app = Flask(__name__)

@app.route('/')
def my_page():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_page2():
	text = request.form['text']
	num = map(int, text.split(','))
	n = len(num)
	num = sort(num)
	return render_template('index.html', a= num)

if __name__ == '__main__':
	app.run('localhost', debug=True)
