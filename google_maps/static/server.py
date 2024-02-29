from flask import Flask


#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__, static_url_path='/custom_static', static_folder='./custom_static_dir')
