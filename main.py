from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <div style="text-align:center; margin-top:50px;">
        <h1>Tugas Flask Sederhana</h1>
        <a href="/penjumlahan"><button style="margin: 10px;">Penjumlahan</button></a>
        <a href="/pengurangan"><button style="margin: 10px;">Pengurangan</button></a>
    </div>
    '''

@app.route('/penjumlahan')
def jumlah_nilai():
    a = 3
    b = 5
    hasil = a + b
    return f'''
    <div style="text-align:center; margin-top:50px;">
        <h2>Hasil Penjumlahan</h2>
        <p>Nilai a: {a}</p>
        <p>Nilai b: {b}</p>
        <p>Hasil: {hasil}</p>
    </div>
    '''

@app.route('/pengurangan')
def pengurangan_nilai():
    a = 13
    b = 6
    hasil = a - b
    return f'''
    <div style="text-align:center; margin-top:50px;">
        <h2>Hasil Pengurangan</h2>
        <p>Nilai a: {a}</p>
        <p>Nilai b: {b}</p>
        <p>Hasil: {hasil}</p>
    </div>
    '''

if __name__ == '__main__':
    app.run()
