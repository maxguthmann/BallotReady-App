from flask import Flask
import psycopg2
from sqlalchemy import create_engine
import sqlalchemy
app= Flask(__name__)

@app.route('/')
def hello():
	engine=create_engine('postgresql://postgres:password@db:5432')
	db = engine.connect()
	db.execute("CREATE TABLE IF NOT EXISTS tab(col INTEGER)")
	db.execute("INSERT INTO tab(col) VALUES(1)")
	result=db.execute("SELECT * FROM tab")
	for r in result:
		return str(r)
	db.close()

app.run(host="0.0.0.0")

