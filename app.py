from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DB1(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    description = db.Column(db.JSON, nullable=False)


@app.route('/', methods=['POST', 'GET'])
def input_data():
    if request.method == 'POST':
        x = request.form['input_text']
        db1 = DB1(description=x)
        try:
            db.session.add(db1)
            db.session.commit()
            db2 = DB1.query.order_by(DB1.id).all()
            return render_template('base.html', db2=db2)
        except:
            return "Что-то пошло не так"
    else:
        return render_template('base.html', description='x')


if __name__ == '__main__':
    app.run(debug=True)

