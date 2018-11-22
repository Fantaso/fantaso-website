from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_security import Security, SQLAlchemyUserDatastore
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
# from flask_mail import Mail
from flask_uploads import IMAGES, UploadSet, configure_uploads
# from fantaso.forms import RegisterFormExt
from fantaso.config import Config

from os.path import dirname, join
from os import getcwd

# def get_path():
#     return join(dirname(__file__)[:-5], 'static/images/crops')
# admin.add_view(FileAdmin(get_path(), '/crops/', name='CropImage'))

app = Flask(__name__)                               # creates the flask app

######## FLASK-UPLOADS ###############
photos_folder_rel_path = 'fantaso/static'
photos_folder_full_path = getcwd()
photos_folder = 'products'

photos =  UploadSet('photos', IMAGES)               # Flask-Uploads
app.config['UPLOADED_PHOTOS_DEST'] = join(photos_folder_rel_path, photos_folder)       # Flask-Uploads
app.config.from_object(Config)                   # imports app configuration from config.py
configure_uploads(app, photos)
######## FLASK-UPLOADS ###############

db = SQLAlchemy(app)                                # create database connection object
migrate = Migrate(app, db)                          # creates a migration object for the app db migrations]\
# mail = Mail(app)

# TO MANAGE THE MIGRATIONS WITH FLASK-SCRIPT WITH PYTHON EXTERNAL SCRIPTS > goes together to migrations for migraing db
# server = Server(host = '192.168.1.17', port = 8000, debug = True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host=None, port=None))


#############################
# Begin Import Models
#############################
from fantaso.bp_shop.models import Product, Order, ProductImage
# from fantaso.bp_shop.models import Product, Order
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
from fantaso.bp_web.views import web
from fantaso.bp_shop.views import shop
from fantaso.bp_admin.views import bp_admin

from fantaso.bp_admin_ext.views import bp_admin_ext


app.register_blueprint(web, url_prefix='/web')
app.register_blueprint(shop, url_prefix='/shop')
app.register_blueprint(bp_admin, url_prefix='/bp_admin')

app.register_blueprint(bp_admin_ext, url_prefix='/admin')
#############################
# End Import Views
#############################
