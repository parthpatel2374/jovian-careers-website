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