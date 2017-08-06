import stripe
from flask import Flask
from flask_restful import Resource, Api
from flask import Response
from flask import request

app = Flask(__name__)
api = Api(app)

class makePayment(Resource):
    def post(self): 
        amount = request.form["amount"]
        source = request.form["source"]
        description = request.form['description']
        stripe.api_key = '<STRIPE SECRET KEY>'#starting with sk...
        print "Attempting charge..."
        resp = stripe.Charge.create(amount=amount, currency='usd', source=source, description=description)
        print 'Success'

api.add_resource(makePayment, '/makePayment/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7002')
