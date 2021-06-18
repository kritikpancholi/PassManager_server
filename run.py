from PassManager import app , db

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host = '192.168.43.77',port=5000)

