

def check_user(username, password):
  db = pymysql.connect("localhost")
  cur = db.cursor()
  cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))

  # If the query returns any matching record, consider the current user logged in.
  record = cursor.fetchone()
  res = False
  if record:
    res = True
  db.close()
  return res


