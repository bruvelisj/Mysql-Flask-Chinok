from flask_cors import CORS
from flask import Flask, jsonify, make_response, send_from_directory
import MySQLdb
#import os
#import json


app = Flask(__name__, static_url_path='/')
#app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello():
    return "<h1>Sveiki!</h1>"


@app.route('/static/<path:path_variable>')
def send_js(path_variable):
    # print(send_from_directory.__doc__)
    return send_from_directory('./HTML/', path_variable)

    # return send_from_directory('/c/Users/Tatjana/Downloads/EDIBO/', path_variable)
    # return send_from_directory('C:\\Users\\Tatjana\\Downloads\\EDIBO\\HTML\\', path_variable)

# db = mysql.connect(
#     host="127.0.0.1",
#     user="root",
#     passwd="Mysqljan****",
#     database="datubaze"
# )
# cursor = db.cursor()

# ufile = open('user.txt', 'r')
# user = ufile.read()[:-1]
# ufile.close()

# pfile = open('password.txt', 'r')
# password = pfile.read()[:-1]
# pfile.close()


@app.route("/select")
def select():
    db = MySQLdb.connect("127.0.0.1", "root", "Mysqljan****", "datubaze")
    cur = db.cursor()
    query = "SELECT * FROM artists WHERE ArtistId >= 1 AND ArtistId <= 10"
    cur.execute(query)
    json_data = cur.fetchall()
    cur.close()
    print("json_data (select):")
    print(json_data)
    return jsonify(data=json_data)


@app.route("/select/<int:id>")
def select_by_id(id):
    db = MySQLdb.connect("127.0.0.1", "root", "Mysqljan****", "datubaze")
    cur = db.cursor()
    query = "SELECT * FROM artists WHERE ArtistId=" + str(id)
    #query = "SELECT * FROM artists WHERE ArtistId=%s" % (id)
    cur.execute(query)
    json_data = cur.fetchall()
    cur.close()
    print("json_data (select):")
    print(json_data)
    return jsonify(data=json_data)


@app.route("/get_customer/<int:id>", methods=['GET'])
def get_customer(id):
    db = MySQLdb.connect("127.0.0.1", "root", "Mysqljan****", "datubaze")
    cur = db.cursor()
    proc = "get_customer"
    cur.callproc(proc, [id])

    columns = [x[0] for x in cur.description]
    print(columns)

    data = cur.fetchall()
    print(data)
    json_data = []
    for result in data:
        json_data.append(dict(zip(columns, result)))
        print(json_data)
    # query = "call datubaze.get_customer(" + id + ")"
    # cur.execute(query)
    # json_data = cur.fetchall()
    cur.close()
    print("json_data (proc):")
    print(json_data)
    response = {'data': json_data}
    return jsonify(data=json_data)


@app.route("/delete_albums/<table>/<int:id>", methods=['DELETE'])
def delete_albums(table, id=None):
    db = MySQLdb.connect("127.0.0.1", "root", "Mysqljan****", "datubaze")
    cur = db.cursor()
    proc = "delete_albums"
    cur.callproc(proc, [id])
    return print " Okey "


# @app.route("/delete_albums/<table>/<int:id>", methods=['DELETE'])
# def delete_albums(table, id=None):
#     db = MySQLdb.connect("127.0.0.1", "root", "Mysqljan****", "datubaze")
#     try:
#         del db[table][id]
#     except:
#         print('returning')


# @app.route("/update_albums/<int:id>/<str:title>", methods=['PUT'])
# def update_albums_by_id(id):
#     db = MySQLdb.connect("127.0.0.1", "root", "Mysqljan****", "datubaze")
#     cur = db.cursor()
#     proc = "update_albums"
#     cur.callproc(proc, [id])

#     data = cur.fetchall()
#         get_
#         if data.get('title'):
#             get_product.title = data['title']
#         if data.get('productDescription'):
#             get_product.productDescription = data['productDescription']
#         if data.get('productBrand'):
#             get_product.productBrand = data['productBrand']
#         if data.get('price'):
#             get_product.price= data['price']
#         db.session.add(get_product)
#         db.session.commit()
#         product_schema = ProductSchema(only=['id', 'title', 'productDescription','productBrand','price'])
#         product = product_schema.dump(get_product)
#         return make_response(jsonify({"product": product}))


if __name__ == '__main__':
    app.run(port=5000)
