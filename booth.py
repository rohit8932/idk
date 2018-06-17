from bitstring import BitArray
from flask import Flask
from flask import request
from flask import render_template



def booth(multiplicand, multiplier, x,y):
	totalLength = x + y + 1
	M1 = BitArray(int=multiplicand, length=totalLength)
	A = M1 << (y+1)
	M2 = BitArray(int=-multiplicand, length=totalLength)
	S = M2 << (y+1)
	print "value of S " + str(S.int)
	P1 = BitArray(int=multiplier, length=y)
	P1.prepend(BitArray(int=0, length=x))
	P = P1 << (1)
	
	for i in range(1, y+1):
		if P[-2:] == '0b01':
			P = BitArray(int=P.int + A.int, length=totalLength)
		elif P[-2:]=='0b10':
			P = BitArray(int=P.int + S.int, length=totalLength)
		P = BitArray(int=(P.int >> 1), length=P.len)
	P = P[:-1]
	return P.bin, P.int


app = Flask(__name__)
@app.route('/')
def my_page():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def my_page2():
	text1 = int (request.form['text1'])
	text2 = int (request.form['text2'])
	n,m = booth(text1, text2, 5,5)
	return "Anser in binary: "+str(n) +"<br>Answer: "+str(m)

if __name__ == '__main__':
	app.run('localhost', debug=True)
