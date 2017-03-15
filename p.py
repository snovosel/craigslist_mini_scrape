from craigslist import CraigslistForSale
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    MAIL_SERVER= 'smtp.gmail.com',
    MAIL_POST = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME= 'cglpizazz@gmail.com',
    MAIL_PASSWORD= 'Flwr1281!',
    MAIL_DEFAULT_SENDER= 'cglpizazz@gmail.com',
)

mail = Mail(app)


@app.route('/')
def index():
	return render_template('index.html')


#retrieve email address from client
@app.route('/register', methods=['POST'] )
def register():
    category = request.form['category']
    email = request.form['email']
    get_info(email, category)
    print email
    return render_template('index.html', items=items)


#send craigslist info to client using email entered in form
def get_info(x):
    items = CraigslistForSale(site='southjersey', category=category, filters={'max_price': 200})
    msg = Message(recipients=[x])
    msg.html = render_template("results.html", items=items)
    mail.send(msg)
    return render_template('results.html', items=items)



if __name__ == "__main__":
	app.run(debug=True)
