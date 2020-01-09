import os
from dataclasses import dataclass


@dataclass(frozen=True)
class OAuthConfig:
    google_client_id: str = os.getenv('google_client_id')
    google_client_secret: str = os.getenv('google_client_secret')
    google_redirect_uri: str = os.getenv('google_redirect_uri')
    kakao_client_id: str = os.getenv('kakao_client_id')
    kakao_client_secret: str = os.getenv('kakao_client_secret')
    kakao_redirect_uri: str = os.getenv('kakao_redirect_uri')
    github_client_id: str = os.getenv('github_client_id')
    github_client_secret: str = os.getenv('github_client_secret')
    github_redirect_uri: str = os.getenv('github_redirect_uri')


@dataclass(frozen=True)
class Config:
    env: str = os.getenv('ENV')
    debug: bool = os.getenv('DEBUG', True)
    app_host: str = os.getenv('APP_HOST', '0.0.0.0')
    app_port: int = os.getenv('APP_PORT', 8000)
    db_user: str = os.getenv('DB_USER', 'codelog')
    db_pass: str = os.getenv('DB_PASS', 'codelog')
    db_host: str = os.getenv('DB_HOST', 'localhost')
    db_name: str = os.getenv('DB_NAME', 'codelog')
    db_url: str = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:3306/{db_name}'
    jwt_secret_key = os.getenv('JWT_SECRET_KEY', 'codelog')
    jwt_algorithm = 'HS256'
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }


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
    env = os.getenv('ENV', 'development')
    config_type = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }
    return config_type[env]
