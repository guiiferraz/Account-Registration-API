from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()


username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
db_name = os.getenv('DB_NAME')

db_url = f"postgresql+psycopg://{username}:{password}@{host}:{port}/{db_name}"


def db_session():
    engine = create_engine(db_url)
    session = Session(engine)

    try:
        with Session(engine) as session:
            result = session.execute(text("SELECT 1"))

            print("Connection with successfully!")

    except Exception as e:
        print(f"Error with connection: {e}")

    return session


db_session()
