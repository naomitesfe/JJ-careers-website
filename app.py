from flask import Flask, render_template, jsonify
from database import engine, load_jobs_from_db
from sqlalchemy import text
app = Flask(__name__)



@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='JJ')
  
@app.route('/api/jobs')
def jobs_list():
  jobs = load_jobs_from_db()
  return jsonify(jobs)
             
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080 , debug=True)
