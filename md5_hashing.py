import md5 # imports the md5 module to generate a hash
password = 'password'
# encrypt the password we provided as 32 character string
hashed_password = md5.new(password).hexdigest()
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!


import md5 # do this at the top of your file where you import modules
@app.route('/users/create', methods=['POST'])
def create_user():
     username = request.form['username']
     email = request.form['email']
     password = md5.new(request.form['password']).hexdigest()
     insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username,
     :email, :password, NOW(), NOW())"
     query_data = { 'username': username, 'email': email, 'password': password }
     mysql.query_db(insert_query, query_data)



password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>


salt = '123' //where the value 123 changes randomly
hashed_password = md5(password + salt)


import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
