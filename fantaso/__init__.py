from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_security import Security, SQLAlchemyUserDatastore
# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
# from flask_mail import Mail
# from flask_uploads import IMAGES, UploadSet, configure_uploads
# from fantaso.forms import RegisterFormExt
from fantaso.config import Config


app = Flask(__name__)                               # creates the flask app
# photos =  UploadSet('photos', IMAGES)               # Flask-Uploads
# app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'       # Flask-Uploads
app.config.from_object(Config)                   # imports app configuration from config.py

# configure_uploads(app, photos)

# db = SQLAlchemy(app)                                # create database connection object
# migrate = Migrate(app, db)                          # creates a migration object for the app db migrations]\
# mail = Mail(app)

# TO MANAGE THE MIGRATIONS WITH FLASK-SCRIPT WITH PYTHON EXTERNAL SCRIPTS > goes together to migrations for migraing db
# server = Server(host = '192.168.1.17', port = 8000, debug = True)
manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# manager.add_command('runserver', Server(host=None, port=None))


#############################
# Begin Import Models
#############################
# from fantaso.models import roles_users, Role, User
# from fantaso.models import Farm, Field, DailyFieldInput, Crop
# from fantaso.models import Agrimodule, Agrisensor, Measurement, Agripump, Pump
#############################
# End Import Models
#############################


#############################
# Begin Setup Flask-Security
#############################
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore, register_form=RegisterFormExt, confirm_register_form=RegisterFormExt)
#############################
# End Setup Flask-Security
#############################


#############################
# Begin Import Views
#############################
from fantaso import views
from fantaso.website_blueprint.views import website_blueprint
# from fantaso.users.views import users
# from fantaso.welcome.views import welcome
# from fantaso.main.views import main
# from fantaso.settings.views import settings
# from fantaso.farm_settings.views import farm_settings
# from fantaso.agrimodule_settings.views import agrimodule_settings
# from fantaso.pump_settings.views import pump_settings
# from fantaso.agrimodule.views import agrimodule_bp
# from fantaso.agripump.views import agripump_bp
# from fantaso.crop_status.views import crop_status
# from fantaso.login_check.views import login_check
# from fantaso.admin.views import admin_bp
# from fantaso.agrimodule_api.views_new import agrimodule_api
# from fantaso.crop_planning.views import crop_planning_bp

app.register_blueprint(website_blueprint, url_prefix='/web')
# app.register_blueprint(users, url_prefix='/users')
# app.register_blueprint(welcome, url_prefix='/welcome')
# app.register_blueprint(main, url_prefix='/main')
# app.register_blueprint(settings, url_prefix='/settings')
# app.register_blueprint(farm_settings, url_prefix='/farm-settings')
# app.register_blueprint(agrimodule_settings, url_prefix='/agrimodule-settings')
# app.register_blueprint(pump_settings, url_prefix='/pump-settings')
# app.register_blueprint(agrimodule_bp, url_prefix='/agrimodule')
# app.register_blueprint(agripump_bp, url_prefix='/agripump')
# app.register_blueprint(crop_status, url_prefix='/crop-status')
# app.register_blueprint(login_check, url_prefix='/login-check')
# app.register_blueprint(admin_bp, url_prefix='/admin')
# app.register_blueprint(agrimodule_api, url_prefix='/agrimodule_api')
# app.register_blueprint(crop_planning_bp, url_prefix='/crop_planning')
#############################
# End Import Views
#############################
