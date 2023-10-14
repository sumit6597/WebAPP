import mysql.connector
import hashlib
import uuid
from flask import Flask, request, render_template
import random
import time

def get_variable_data(query, values):
    connection = mysql.connector.connect(user='root', password='Sumit@6597', host='127.0.0.1', database='LIONPATH')
    cursor = connection.cursor()
    cursor.execute(query, values)
    results = [row for row in cursor]
    connection.close()
    return results

def get_checkin_data(email): 
    # create a connection
    cnx = mysql.connector.connect(user='root', password='Sumit@6597', host='127.0.0.1', database='LIONPATH')
    cursor = cnx.cursor()

    query = "SELECT B.email, B.first_name, B.last_name, B.gender, B.age, A.zipcode AS home_zipcode, A.street_name AS home_street, Z.city AS home_city, Z.state_id AS home_state, A1.zipcode AS billing_zipcode, A1.street_name AS billing_street, Z1.city AS billing_city, Z1.state_id AS billing_state FROM Bidders B JOIN Address A ON B.home_address_id = A.address_id JOIN Zipcode_Info Z ON A.zipcode = Z.zipcode JOIN Address A1 ON B.home_address_id = A1.address_id JOIN Zipcode_Info Z1 ON A1.zipcode = Z1.zipcode WHERE B.email = %s"
    cursor.execute(query,(email,))
    result = list()

    for row in cursor:
        result.append(row)
    cnx.close()
    return result # getting user info for input.html

def update(query, tuple):
    # create a connection
    cnx = mysql.connector.connect(user='root', password='Sumit@6597', host='127.0.0.1', database='LIONPATH')
    cursor = cnx.cursor()
    cursor.execute(query,tuple)
    cnx.commit()
    cnx.close()
    return True

def get_data(query):
    # create a connection
    cnx = mysql.connector.connect(user='root', password='Sumit@6597', host='127.0.0.1', database='LIONPATH')
    cursor = cnx.cursor()
    cursor.execute(query)
    result = list()

    for row in cursor:
        result.append(row)
    cnx.close()
    return result

def check_for_data(query, tuple):
    # create a connection
    cnx = mysql.connector.connect(user='root', password='Sumit@6597', host='127.0.0.1', database='LIONPATH')
    cursor = cnx.cursor()
    cursor.execute(query,tuple)
    result = list()

    for row in cursor:
        result.append(row)
    cnx.close()
    return result

app = Flask(__name__)

@app.route('/')
def index():
    query = "SELECT DISTINCT(category) FROM Categories WHERE parent = 'Root';"
    categories = get_data(query)

    query = "SELECT * FROM Auction_Listings"
    products = get_data(query)

    result = (categories, products)
    return render_template('index.html', result=result)

@app.route('/choice', methods=['POST'])
def choice():

    choice = request.form['category']
    query = "SELECT DISTINCT(category) FROM Categories WHERE parent = %s ;"
    categories = get_variable_data(query, (choice,))

    res = [''.join(i) for i in categories]
    res.append(choice)

    query = "SELECT * FROM Auction_Listings WHERE category IN ('" + '\',\''.join(res) + "');"
    products = get_data(query)

    result = (categories, products)
    return render_template('index.html', result=result)


@app.route('/login', methods=['POST'])
def test():
    email = request.form['uname']
    password = hashlib.sha256(request.form['psw'].encode()).hexdigest()
    query_tu = (email, password)

    query = "SELECT count(*) FROM Users WHERE email = %s and password = %s;"
    result = get_variable_data(query, query_tu)

    is_one = result[0][0]
    
    if(is_one==1):
        info = get_checkin_data(email)
        isSeller = False
        isBidder = True

        tuple = (email,)
        query = "SELECT * FROM Sellers WHERE email=%s"
        tuple = (email,)
        if(check_for_data(query,tuple)):
            isSeller = True
        cbq = "SELECT * FROM Bidders WHERE email=%s"
        tuple = (email,)
        if not (check_for_data(cbq,tuple)):
            isBidder = False
            info = [(email, 'User', 'Seller', ' ', 000, '', 'NA', '', '', '', 'NA', '', '')]
        result = (info, isSeller)
        return render_template('input.html', result=result)
    else:
        query = "SELECT DISTINCT(category) FROM Categories WHERE parent = 'Root';"
        categories = get_data(query)

        query = "SELECT * FROM Auction_Listings"
        products = get_data(query)

        result = (categories, products)

        return render_template('index.html', error="Wrong Credentials",result=result)


@app.route('/update_password', methods=['POST'])
def update_password():
    password = request.form['password']
    password_copy = request.form['re_password']
    email = request.form['email']

    if(password != password_copy):
        return render_template('input.html', error="Password Mismatch")
    password = hashlib.sha256(request.form['password'].encode()).hexdigest()
    query_tuple = (password, email)
    query = "UPDATE Users SET password = %s WHERE email = %s;"

    update(query, query_tuple)
    result = get_checkin_data(email)
    hurray=True
    result = (result, False)
    return render_template('input.html', message=hurray, result=result)



@app.route('/update_listing', methods=['POST'])
def update_listing():
    category = request.form['category']
    # print(category)
    title = request.form['title']
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    price = request.form['reserve_price']
    # print(price)
    quantity = request.form['quantity']
    
    max_bids = request.form['max_bids']
    listing_status = request.form['listing_status']
    email = request.form['email']

    query_tuple = (email, str(uuid.uuid4()), category, title, product_name, product_description,  quantity, price, max_bids,listing_status)
    query = "INSERT INTO Auction_Listings VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    update(query, query_tuple)
    result = get_checkin_data(email)

    result = get_checkin_data(email)
    cbq = "SELECT * FROM Bidders WHERE email=%s"
    tuple = (email,)
    if not (check_for_data(cbq,tuple)):
        isBidder = False
        result= [(email, 'User', 'Seller', ' ', 000, '', 'NA', '', '', '', 'NA', '', '')]

    result = (result, True)
    return render_template('input.html', result=result)




def generate_unique_number():
    timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
    random_num = random.randint(0, 1000)  # Generate a random number between 0 and 1000
    unique_num = (timestamp << 10) + random_num  # Combine timestamp and random number
    return unique_num

@app.route('/submit_request', methods=['POST'])
def submit_request():
    id= generate_unique_number()
    sender_email = request.form['email']
    request_type = request.form['request_type']
    request_desc = request.form['request_desc']
    request_status = request.form['request_status']

    # determine recipient email based on request type
    if request_type == 'ChangeID':
        recipient_email = 'tplutherot@lsu.edu'
    elif request_type == 'MarketAnalysis':
        recipient_email = 'helpdeskteam@lsu.edu'
    elif request_type == 'AddCategory':
        recipient_email = 'helpdeskteam@lsu.edu'

    query_tuple = (id, sender_email, recipient_email, request_type, request_desc, request_status)
    query = "INSERT INTO Requests VALUES (%s, %s, %s, %s, %s, %s);"  
    update(query, query_tuple)  

    result = get_checkin_data(sender_email)
    cbq = "SELECT * FROM Bidders WHERE email=%s"
    tuple = (sender_email,)
    if not (check_for_data(cbq,tuple)):
        isBidder = False
        result= [(sender_email, 'User', 'Seller', ' ', 000, '', 'NA', '', '', '', 'NA', '', '')]
    result = (result, True)

    return render_template('input.html', result=result)




# main driver function
if __name__ == '__main__':
    app.run(port=8080, debug=True)