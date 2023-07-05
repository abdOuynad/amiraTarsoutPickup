from flask import Blueprint,render_template,redirect,url_for
#
main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder = '../templates',
    url_prefix= '/'
)
#
@main_blueprint.route('/')
def home():
    #
    return redirect(url_for('pickup.index'))
    #
#