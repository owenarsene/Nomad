// pip install flask flask-login flask-sqlalchemy flask-mail flask-dance
// figma installation for Flask import redirect request_url, flash and session 
// itsdangerouse import SQLAlchemy 

from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from flask_dance.contrib.google import make_google_blueprint, google
import os
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)
#輸入提示詞後轉換至設定介面

# Google OAuth2 設定
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # 開發用，不加密
google_bp = make_google_blueprint(client_id="YOUR_GOOGLE_CLIENT_ID",
                                  client_secret="YOUR_GOOGLE_CLIENT_SECRET",
                                  redirect_to="google_login")
app.register_blueprint(google_bp, url_prefix="/google_login")

# 時間戳工具（生成和驗證令牌） 
# 串接wix API設定
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])


# 用戶模型
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    google_id = db.Column(db.String(200), nullable=True)  # Google 帳號綁定

# 初始化數據庫
db.create_all()


//coordinate program technic
