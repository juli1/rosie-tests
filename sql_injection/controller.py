from sql_injection.database import check_user


@app.route("/login")
def login():

  username = request.values.get('username')
  password = request.values.get('password')

  if check_user(username, password):
    session['logged_user'] = username

