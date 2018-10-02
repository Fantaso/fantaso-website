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
    return render_template('bp_web/index.html')

##################
# SERVICES
##################
@web.route('/services', methods=['GET'])
def services():
    return render_template('bp_web/services.html')

##################
# INDUSTRIES
##################
@web.route('/industries', methods=['GET'])
def industries():
    return render_template('bp_web/industries.html')

##################
# PROJECTS
##################
@web.route('/projects', methods=['GET'])
def projects():
    return render_template('bp_web/projects.html')

##################
# ABOUT
##################
@web.route('/about', methods=['GET'])
def about():
    return render_template('bp_web/about.html')

##################
# BLOG
##################
@web.route('/blog', methods=['GET'])
def blog():
    return render_template('bp_web/blog.html')

##################
# CONTACT
##################
@web.route('/contact', methods=['GET'])
def contact():
    return render_template('bp_web/contact.html')
