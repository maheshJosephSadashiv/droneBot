import apscheduler
from flask import Flask
from extensions import db, ma, scheduler
from scheduler import droneScheduler
from routes import bp
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
CORS(app)
db.init_app(app)
ma.init_app(app)

try:
    scheduler.add_job(droneScheduler.schedule, 'interval', seconds=30, args=[app.app_context()])
    scheduler.start()
except apscheduler.schedulers.SchedulerAlreadyRunningError:
    pass

if __name__ == "__main__":
    app.register_blueprint(bp)
    app.run(debug=True)
