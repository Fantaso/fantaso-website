from flask import Blueprint, render_template, redirect, url_for, flash


web = Blueprint(
    'web',
    __name__,
    template_folder='templates',
    # static_folder='static',
)


##################
# INDEX
##################
@web.route('/', methods=['GET'])
def index():
    return render_template('web_blueprint/index.html')

##################
# SERVICES
##################
@web.route('/services', methods=['GET'])
def services():
    return render_template('web_blueprint/services.html')

##################
# INDUSTRIES
##################
@web.route('/industries', methods=['GET'])
def industries():
    return render_template('web_blueprint/industries.html')

##################
# PROJECTS
##################
@web.route('/projects', methods=['GET'])
def projects():
    return render_template('web_blueprint/projects.html')

##################
# ABOUT
##################
@web.route('/about', methods=['GET'])
def about():
    return render_template('web_blueprint/about.html')

##################
# BLOG
##################
@web.route('/blog', methods=['GET'])
def blog():
    return render_template('web_blueprint/blog.html')

##################
# CONTACT
##################
@web.route('/contact', methods=['GET'])
def contact():
    return render_template('web_blueprint/contact.html')
