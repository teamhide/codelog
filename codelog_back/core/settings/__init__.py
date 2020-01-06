import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    env: str
    debug: bool = os.getenv('DEBUG', True)
    app_host: str = os.getenv('APP_HOST', '0.0.0.0')
    app_port: int = os.getenv('APP_PORT', 5000)
    db_user: str = os.getenv('DB_USER', 'codelog')
    db_pass: str = os.getenv('DB_PASS', 'codelog')
    db_host: str = os.getenv('DB_HOST', 'localhost')
    db_name: str = os.getenv('DB_NAME', 'codelog')
    db_url: str = os.getenv(
        'DB_URL',
        f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:3306/{db_name}',
    )
    jwt_secret_key = os.getenv('JWT_SECRET_KEY', 'codelog')
    jwt_algorithm = 'HS256'


@dataclass(frozen=True)
class DevelopmentConfig(Config):
    env: str = 'development'
    debug: bool = True
    jwt_secret_key = 'codelog'
    jwt_algorithm = 'HS256'


@dataclass(frozen=True)
class TestingConfig(Config):
    env: str = 'testing'
    debug: bool = True
    jwt_secret_key = 'codelog'
    jwt_algorithm = 'HS256'


@dataclass(frozen=True)
class ProductionConfig(Config):
    env: str = 'production'
    debug: bool = False
    jwt_algorithm = 'HS256'


def get_config():
    env = os.getenv('env', 'development')
    config_type = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }
    return config_type[env]
