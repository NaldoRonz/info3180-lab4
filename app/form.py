from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename


class UploadForm(FlaskForm):
    pics =  FileField(validators = [FileRequired(), FileAllowed(['jpg','png','jpeg'])])

class LoginForm(FlaskForm):
	username = StringField(validators = [DataRequired()])
	password = PasswordField(validators = [DataRequired()])
