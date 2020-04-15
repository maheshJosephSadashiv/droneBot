from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()
ma = Marshmallow()
scheduler = BackgroundScheduler(daemon=True)