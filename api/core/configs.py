from sqlalchemy.orm import declarative_base


class Settings:
    TITLE: str = "FastAPI and SQL Alchemy - Roteiro Promo"
    API_V1_STR: str = "api/v1"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"
    DB_URL: str = "mysql+asyncmy://root:bel468608@localhost:3306/roteiropromo"
    DBBaseModel = declarative_base()

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

# POSTGRE STRING CONNECTION: "postgresql+asyncpg://postgres:bel468608@localhost:5432/roteiropromo"
