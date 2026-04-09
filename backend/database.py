from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Neon PostgreSQL connection URL
DATABASE_URL = "postgresql://neondb_owner:npg_GEqr9KCu7jop@ep-old-frog-amvt0qad-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# PostgreSQL engine — no extra connect_args needed unlike SQLite
engine = create_engine(DATABASE_URL)

# Factory that creates new DB sessions for each request
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# All models inherit from this Base so SQLAlchemy can track them as tables
Base = declarative_base()
