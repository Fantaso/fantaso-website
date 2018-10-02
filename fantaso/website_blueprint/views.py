from flask import Blueprint, render_template, redirect, url_for, flash


website_blueprint = Blueprint(
    'website_blueprint',
    __name__,
    template_folder='templates',
)


##################
# INDEX
##################
@website_blueprint.route('/', methods=['GET'])
def index():
    return render_template('website_blueprint/index.html')

##################
# SERVICES
##################
@website_blueprint.route('/services', methods=['GET'])
def services():
    return render_template('website_blueprint/services.html')

##################
# INDUSTRIES
##################
@website_blueprint.route('/industries', methods=['GET'])
def industries():
    return render_template('website_blueprint/industries.html')

##################
# PROJECTS
##################
@website_blueprint.route('/projects', methods=['GET'])
def projects():
    return render_template('website_blueprint/projects.html')

##################
# ABOUT
##################
@website_blueprint.route('/about', methods=['GET'])
def about():
    return render_template('website_blueprint/about.html')

##################
# BLOG
##################
@website_blueprint.route('/blog', methods=['GET'])
def blog():
    return render_template('website_blueprint/blog.html')

##################
# CONTACT
##################
@website_blueprint.route('/contact', methods=['GET'])
def contact():
    return render_template('website_blueprint/contact.html')
