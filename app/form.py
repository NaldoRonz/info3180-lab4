from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    pics =  FileField(validators=[FileRequired()])
