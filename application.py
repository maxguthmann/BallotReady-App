from flask import Flask
import psycopg2

app= Flask(__name__)

@app.route('/')
def hello():
	conn=psycopg2.connect(host='db', user='postgres')
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS tab(col INTEGER)")
	cur.execute("INSERT INTO tab(col) VALUES(1)")
	conn.commit()
	cur.execute("SELECT * FROM tab")
	result=cur.fetchone()
	return str(result)



app.run(host="0.0.0.0")

