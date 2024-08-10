from flask import Flask, render_template

app = Flask(__name__)

data1 = ["I", "G", "S"]

@app.route('/')
def home():
    biodata = {
        'nama': 'william',
        'umur': 16,
        'pekerjaan': 'cari uang',
        'hobi': 'coding'
    }
    return render_template('home.html', biodata=biodata)

@app.route('/igs')
def igs():
    return render_template('igs.html', data=data1)

if __name__ == '__main__':
    app.run(debug=True)

