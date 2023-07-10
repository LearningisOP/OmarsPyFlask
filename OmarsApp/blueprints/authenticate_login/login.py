@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)

@app.route("/regform")
def regform():
    name = request.args.get("name", "world")
    return render_template("registrationform.html", name=name)

@app.route("/AboutMe")
def about():
    return render_template("about.html")

@app.route("/registrants")
def registrants():
    with open("registered.csv", "r") as file: # using with handles the closing of the file for you
        reader = csv.reader(file)
        students = list(reader)
        return render_template("registrants.html", students = students)


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    file = open("registered.csv", "a") # the a appends to the file
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("dorm")))
    file.close()
    return render_template("success.html")