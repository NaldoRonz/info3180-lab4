from flask import Flask
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

# Config Values
USERNAME = 'Naldo'
PASSWORD = 'Cool'

UPLOAD_FOLDER = "./app/static/uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'vhudw9e2197!3H)_qIps>?Qks0an*#KD_@_XJ!de3G(47^_2sn!mc0nlZnbBhb(cs8KxL^3'	

app = Flask(__name__)
app.config.from_object(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

csrf.init_app(app)

from app import views
