from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    pics =  FileField()

class LoginForm(FlaskForm):
	username = StringField(validators = [DataRequired()])
	password = PasswordField(validators = [DataRequired()])
