from flask import Blueprint

admin = Blueprint(
    'admin',
    __name__,
    template_folder='pages',
    static_folder='static'
)
# 一定要记得导入，因为导入时会执行一遍脚本，在执行脚本时通过装饰器注册路由
from .views import user
