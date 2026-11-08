from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def beranda():
    # Ambil nama hanya setelah formulir dikirim.
    nama = request.form.get("nama", "").strip() if request.method == "POST" else ""
    waktu_server = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return render_template("index.html", nama=nama, waktu_server=waktu_server)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)