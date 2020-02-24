from flask import Flask
from werkzeug.utils import secure_filename

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

UPLOAD_FOLDER = "./app/static/uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'WSJFR2hgu_f3ei%dn7dES6NJSC85'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
