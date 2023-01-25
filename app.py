from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
from flask import send_from_directory

app = Flask(__name__)
app.secret_key = "djfljdfljfnkjsfhjfshjkfjfjfhjdhfdjhdfu"

userpass = "mysql+pymysql://root:@"
basedir = "127.0.0.1"
dbname = "/company"

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Employes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telp = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, telp, address, filename):
        self.name = name
        self.email = email
        self.telp = telp
        self.address = address
        self.filename = filename

@app.route('/index')
def index():
    data_employe = db.session.query(Employes)
    return render_template('index.html', data=data_employe)

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        telp = request.form['telp']
        address = request.form['address']
        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        add_data = Employes(name, email, telp, address, filename)
        
        db.session.add(add_data)
        db.session.commit()

        flash("Input Data Success")

        return redirect(url_for('index', name=filename))

    return render_template('input.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/edit/<int:id>')
def edit_data(id):
    data_employes = Employes.query.get(id)
    return render_template('edit.html', data=data_employes)

@app.route('/proses_edit', methods=['POST', 'GET'])
def proses_edit():
    data_employes = Employes.query.get(request.form.get('id'))

    data_employes.name = request.form['name']
    data_employes.email = request.form['email']
    data_employes.telp = request.form['telp']
    data_employes.address = request.form['address']
    if request.method == 'POST' :
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data_employes.filename = filename
    else :
        data_employes.filename = request.form['file']   

    db.session.commit()

    flash('Edit Data Success')

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    data_employe = Employes.query.get(id)
    db.session.delete(data_employe)
    db.session.commit()

    flash('Delete Data Success')

    return redirect(url_for('index'))

# koneksi
app.secret_key = 'bebasapasaja'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'company'
mysql = MySQL(app)

# registrasi
@app.route('/registrasi', methods=('GET', 'POST'))
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # cek username atau email
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM tb_users WHERE username=%s OR email=%s', (username, email))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO tb_users VALUES (NULL, %s, %s, %s)',
                            (username, email, generate_password_hash(password)))
            mysql.connection.commit()
            flash('Registrasi Berhasil', 'success')
        else:
            flash('Username atau email sudah ada', 'danger')
    return render_template('registrasi.html')


# login
@app.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # cek data username
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_users WHERE email=%s', (email, ))
        akun = cursor.fetchone()
        if akun is None:
            flash('Login Gagal, Cek Username Anda', 'danger')
        elif not check_password_hash(akun[3], password):
            flash('Login gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun[1]
            return redirect(url_for('index'))
    return render_template('login.html')


# logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)