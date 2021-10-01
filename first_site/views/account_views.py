import flask

from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

######## INDEX ########
@blueprint.route('/account')
@reponse(template_file='account/index.html')
def index():
    return {}

######## REGISTER ########
@blueprint.route('/account/register', methods=['GET'])
@reponse(template_file='account/register.html')
def register_get():
    return {}

@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    return {}

######## LOGIN ########
@blueprint.route('/account/login', methods=['GET'])
@reponse(template_file='account/login.html')
def login_get():
    return {}

@blueprint.route('/account/login', methods=['POST'])
@reponse(template_file='account/login.html')
def login_POST():
    return {}

######## LOGOUT ########
@blueprint.route('/account/logout')
def logout():
    return {}