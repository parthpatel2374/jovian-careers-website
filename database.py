from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    # connect_args={
    #     "ssl": {
    #         "ssl_ca": ""
    #     }
    # }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            row_as_dict = row._asdict()
            jobs.append(dict(row_as_dict))

        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id = :val").bindparams(val=id)
        )
        rows = result.all()
        if(len(rows) == 0):
            return None
        else:
            row_as_dict = rows[0]._asdict()
            return row_as_dict