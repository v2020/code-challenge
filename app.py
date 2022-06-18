from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    template_name = "pages/dashboard.html"
    return render_template(template_name)


@app.route("/vulnerabilities/")
def vulnerabilities():
    template_name = "pages/vulnerability_list.html"
    return render_template(template_name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
