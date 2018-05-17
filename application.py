from flask import Flask
import psycopg2
from sqlalchemy import create_engine
import sqlalchemy
app= Flask(__name__)

@app.route('/')
def hello():
	#conn=psycopg2.connect(host='db', user='postgres')
	engine=create_engine('postgresql://postgres:password@db:5432')
	db = engine.connect()
	db.execute("CREATE TABLE IF NOT EXISTS tab(col INTEGER)")
	db.execute("INSERT INTO tab(col) VALUES(1)")
	result=db.execute("SELECT * FROM tab")
	for r in result:
		return str(r)
	db.close()
	#cur=conn.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS tab(col INTEGER)")
	#cur.execute("INSERT INTO tab(col) VALUES(1)")
	#conn.commit()
	#cur.execute("SELECT * FROM tab")
	#result=cur.fetchone()
	



app.run(host="0.0.0.0")

