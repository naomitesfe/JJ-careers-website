from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())  
    return jobs
      
