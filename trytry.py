from flask import Flask, render_template, request
#from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploadimage', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded successfully'


if __name__ == '__main__':

   app.run(threaded=True)