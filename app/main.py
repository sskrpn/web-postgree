from fastapi import FastAPI, Depends, Response
from sqlalchemy.orm import Session
from sqlalchemy import text
import logging
from app.database import get_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Visit Counter",
    version="1.0.0"
)


@app.get("/")
async def root(db: Session = Depends(get_db)):
    db.execute(text("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            visit_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """))
    db.commit()
    
    insert_query = text("INSERT INTO visits (visit_time) VALUES (DEFAULT) RETURNING id")
    result = db.execute(insert_query)
    db.commit()
    
    new_id = result.scalar()
    logger.info(f"Добавлена запись с ID: {new_id}")
    
    count_query = text("SELECT COUNT(*) FROM visits")
    visit_count = db.execute(count_query).scalar()
    
    return Response(
        content=f"Hello! I have been visited {visit_count} times\n test",
        media_type="text/plain"
    )
