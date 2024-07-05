import os


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SENTRY_DSN = os.getenv("SENTRY_DSN")
    DEBUG = True


class ProductionConfig(Config):
    pass


AppConfig = DevelopmentConfig
