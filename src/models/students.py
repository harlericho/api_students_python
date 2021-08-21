from config.db import get_connection

# GET
def list(db):
    try:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM students")
        return cur.fetchall()
    except Exception as e:
        return e
    finally:
        cur.close()


# GET {ID}
def listId(db, id):
    try:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM students WHERE id={0}".format(id))
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()

# POST
def post(db, names, email,age):
    try:
        cur = db.connection.cursor()
        cur.execute("INSERT INTO students (names, email, age) VALUES('{0}','{1}',{2})".format(names, email, age))
        return db.connection.commit()
    except Exception as e:
        return e
    finally:
        cur.close()

# UPDATE
def put(db, names, email,age,id):
    try:
        cur = db.connection.cursor()
        cur.execute("UPDATE students SET names='{0}',email='{1}',age={2} WHERE id={3}".format(names, email, age,id))
        return db.connection.commit()
    except Exception as e:
        return e
    finally:
        cur.close()

# DELETE{ID}
def delete(db, id):
    try:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM students WHERE id={0}".format(id))
        return db.connection.commit()
    except Exception as e:
        return e
    finally:
        cur.close()