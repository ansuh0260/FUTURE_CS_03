from flask import Flask, request, send_file, render_template
from encryption_utils import encrypt_file, decrypt_file
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv("SECRET_KEY").encode('utf-8')  # Must be 16, 24, or 32 bytes

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    enc_path = file_path + ".enc"
    file.save(file_path)
    encrypt_file(file_path, enc_path, KEY)
    os.remove(file_path)
    return f"File encrypted and saved as {file.filename}.enc"

@app.route('/download', methods=['POST'])
def download():
    filename = request.form['filename']
    enc_path = os.path.join(UPLOAD_FOLDER, filename)
    dec_path = enc_path.replace(".enc", "")
    decrypt_file(enc_path, dec_path, KEY)
    return send_file(dec_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
