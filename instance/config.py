import os

class DevConfig:
    """ Parent Configuration Class"""
    DEBUG = True
    SECRET_KEY = 'nova_catharge_hasdrubal-260BC-200BCE'
    CSRF_ENABLED = True
    TEST = False


class DevelopmentConfig(DevConfig):
    """Configuration for development"""
    DEBUG = True
    DATABASE_URI = os.getenv("DATABASE_URL")

class TestingConfig(DevConfig):
    """Configuration for Testing"""
    TEST = True
    DEBUG = True
    DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class ProductionConfig(DevConfig):
    """Configuration for production"""
    DEBUG = True
    TESTING = False 

CONFIGS = {
    'development_config': DevelopmentConfig,
    'testing_config': TestingConfig
}


