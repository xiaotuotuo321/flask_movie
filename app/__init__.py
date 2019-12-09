from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册
app.register_blueprint(home_blueprint)  # 前台不需要url_prefix
app.register_blueprint(admin_blueprint, url_prefix="/admin")
