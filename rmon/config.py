"""rmon.config
rmon 配置文件
"""
import os


class DevConfig:
    """开发环境配置
    """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URL = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = True


class ProductConfig(DevConfig):
    """生产环境配置
    """
    DEBUG = False
    path = os.path.join(os.getcwd(), 'rmon.db').replace('\\', '/')
    SQLALCHEMY_DATABASE_URL = 'sqlite:///%s' % path
