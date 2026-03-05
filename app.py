import psycopg2
from sqlalchemy import create_engine, text

# PostgreSQL connection
engine = create_engine('postgresql://user:password@db:5432/mydb')

# Test connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT version()"))
    print("PostgreSQL version:", result.fetchone()[0])

print("Connected to PostgreSQL successfully!")