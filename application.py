from flask import Flask
import psycopg2

app= Flask(__name__)

@app.route('/')
def hello():
	conn=psycopg2.connect(host='postgres', user='postgres')
	cur=conn.cursor()
	cur.execute("CREATE TABLE tab(col INTEGER)")
	cur.execute("INSERT INTO tab(col) VALUES(1,2,3)")
	conn.commit()
	cur.execute("SELECT * FROM tab")
	result=cur.fetchall()
	return result



app.run(host="0.0.0.0")

