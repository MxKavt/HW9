from flask import Flask
from flask_restful import Resource, Api
import sqlite3


app = Flask(__name__)
api = Api(app)


class Students(Resource):
    def get(self, student_id):
        con = sqlite3.connect("identifier.sqlite")
        cur = con.cursor()
        cur.execute("SELECT * FROM students where id = ?", (student_id,))
        return cur.fetchall()


api.add_resource(Students, '/', '/get/<int:student_id>')


# port=8080 or any other port doesn't work
if __name__ == "__random_app":
    app.run(debug=True)






# personal notes

#CRUD = create read update and delete
# --------------------------------------------------------------------------------------------------------
                                                                                            # C for Create
# 1 way
# for s in [(3, "student_3", "", 21), (4,"student_4", "", 21)]:
#     cur.execute("""INSERT INTO students (id, name, course, age)
#                     values (?, ?, ?, ?)""", (s[0], s[1], s[2], s[3]))
#     con.commit()
# 2 way
# cur.executemany("INSERT INTO students (id, name, course, age) values (?, ?, ?, ?)", [(4, "student_4", "", 21), (6,"student_6", "", 21)])
# con.commit()
# --------------------------------------------------------------------------------------------------------
                                                                                              # R for Read
# cur.execute("SELECT * FROM students where name = 'student_3'")
# print(cur.fetchall())
# cur.execute("SELECT * FROM students")
# print(cur.fetchone())
# --------------------------------------------------------------------------------------------------------
                                                                                            # U for Update
# # cur.execute("UPDATE students set name = ? where id=?", ("student_6", 6))
# # con.commit()
# --------------------------------------------------------------------------------------------------------
                                                                                            # D for Delete
# cur.execute("Delete from students where id in (?, ?)", (4,6))
# con.commit()
# --------------------------------------------------------------------------------------------------------
