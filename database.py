from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://admin:esFQCENu@mysql-148941-0.cloudclusters.net:19360/jjcareers")

def load_jobs_from_db():
    
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())  
    return jobs
      
