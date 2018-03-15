from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/student")
def student():
	return render_template("student.html")

@app.route("/admin")
def admin():
	return render_template("admin.html")

@app.route("/usn", methods=["POST",'GET'])
def usn():
	if request.method == "GET":
		return "Please submit the form instead"
	else:
		name = request.form.get("usn")
		return render_template("usn.html",name=name)


if (__name__ == "__main__"):
    app.run(port = 5000)

