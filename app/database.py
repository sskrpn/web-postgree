import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Отсутствует переменная окружения: {key}")
    return value

DB_HOST = get_required_env("DB_HOST")
DB_PORT = get_required_env("DB_PORT")
DB_NAME = get_required_env("DB_NAME")
DB_USER = get_required_env("DB_USER")
DB_PASSWORD = get_required_env("DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()