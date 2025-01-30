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
acces_db = os.getenv('ACCESS_DB')


def db_session():
    if acces_db == 'test':
        db_url = os.getenv('DB_URL_TEST')
    else:
        db_url = f"postgresql+psycopg://{username}:{password}@{host}:{port}/{db_name}"

    engine = create_engine(db_url)
    session = Session(engine)

    try:
        with Session(engine) as session:
            result = session.execute(text("SELECT 1"))

            print("Connection with successfully!")

    except Exception as e:
        print(f"Error with connection: {e}")

    return session
