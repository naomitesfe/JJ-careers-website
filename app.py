from flask import Flask, render_template, jsonify
from database import engine, load_job_from_db,load_jobs_from_db
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


@app.route('/api/jobs/<id>')
def show_job(id):
  job = load_job_from_db(id)
  return render_template('jobpage.html', job=job)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080 , debug=True)
