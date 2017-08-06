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
class saveCustomer(Resource):
        def post(self):
                email = request.form["email"]
                source = request.form["source"]
        		stripe.api_key = '<STRIPE SECRET KEY>'#starting with sk...
    	        customer = stripe.Customer.create(email=email,source=source)
                print 'Success'
                return customer.id

class payWithCustomer(Resource):
        def post(self):
                amount = request.form["amount"]
                customerId = request.form["customerId"]
                description = request.form['description']
		        stripe.api_key = '<STRIPE SECRET KEY>'#starting with sk...
                charge = stripe.Charge.create( amount=amount,currency="usd",customer=customerId,description=description)



api.add_resource(makePayment, '/makePayment/')
api.add_resource(saveCustomer, '/saveCustomer/')
api.add_resource(payWithCustomer, '/payWithCustomer/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7002')
