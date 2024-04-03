from flask import Flask, request, render_template

app = Flask(__name__)
users = []


@app.route("/<name>/<int:age>/<gender>")
def welcome(name, age, gender):
    return "A"
    # return render_template("login.html", name=name, age=age, gender=gender)


@app.route("/hello")
def hello():
    return "Hello world"


@app.route("/hello/<some_name>")
def name(some_name):
    return f"hello {some_name}!"


@app.route("/reviews/<float:rating>")
def find_reviews(rating):
    return f"Ищем отзывы с рейтингом: {rating}"


@app.route("/age/<int:age>")
def print_age(age):
    return f"Возраст:{age}"


@app.route("/post", methods=["POST"])
def only_post_route():
    return "Only post"


@app.route("/get", methods=["GET"])
def only_get_route():
    return "Only get"


@app.route("/get-post", methods=["GET", "POST"])
def get_post_route():
    if request.method == "GET":
        return "HTML PAGE"
    elif request.method == "POST":
        # a
        return "123"


@app.route("/login", methods=["GET", "POST"])
def login():
    # request.args можно вытаскивать QUERY ПАРАМЕТРЫ
    # return f"{request.args}, {request.args['username']}, {request.args.get('username')}"
    if request.method == "GET":
        return render_template("login.html")
    else:
        local_user = [
            request.form.get("username"),
            request.form.get("password"),
            request.form.get("phone"),
        ]
        users.append(local_user)

        return f"username: {request.form.get('username')}. Password:{request.form.get('password')}  Phone:{request.form.get('phone')}"


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", users=users)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
