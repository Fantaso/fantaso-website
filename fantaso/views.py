from flask import redirect, url_for
from fantaso import app

#############################
# APP INDEX
#############################
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('web.index'))
