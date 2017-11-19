import stripe
from flask import Flask
from flask_restful import Resource, Api
from flask import Response
from flask import request

app = Flask(__name__)
api = Api(app)
stripe.api_key = 'sk_test_niO0JzhN91qTkReKgoUDLJk4'        #starting with sk...
class makePayment(Resource):
    def post(self):
        amount = request.form["amount"]
        source = request.form["source"]
        description = request.form['description']
        print ("Attempting charge...")
        resp = stripe.Charge.create(amount=amount, currency='usd', source=source, description=description)
        print ('Success')
class saveCustomer(Resource):
    def post(self):
        email = request.form["email"]
        source = request.form["source"]
		# stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'#starting with sk...
        customer = stripe.Customer.create(email=email,source=source)
        print ('Success')
        return customer.id

class payWithCustomer(Resource):
    def post(self):
        amount = request.form["amount"]
        customerId = request.form["customerId"]
        description = request.form['description']
        # stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'#starting with sk...
        charge = stripe.Charge.create( amount=amount,currency="usd",customer=customerId,description=description)

class createConnectAccount(Resource):
    def post(self):
        email = request.form["email"]
        account = stripe.Account.create(
          type="standard",
          country="US",
          email=email
        )
        return account

class connectCharge(Resource):
    def post(self):
        amount = request.form["amount"]
        source = request.form["source"]
        account = request.form["account"]
        charge = stripe.Charge.create(
          amount=amount,
          currency="usd",
          source=source,
          destination={
            "amount":amount - 100,
            "account": account,
          }
        )



api.add_resource(makePayment, '/makePayment/')
api.add_resource(saveCustomer, '/saveCustomer/')
api.add_resource(payWithCustomer, '/payWithCustomer/')
api.add_resource(createConnectAccount,'/createConnectAccount/')
api.add_resource(connectCharge,'/connectCharge/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7002')



#     {
#   "business_logo": null,
#   "business_name": null,
#   "business_url": null,
#   "charges_enabled": true,
#   "country": "US",
#   "default_currency": "usd",
#   "details_submitted": false,
#   "display_name": null,
#   "email": "anujshah@example.com",
#   "id": "acct_1BPimwFoXAjDWm3C",
#   "keys": {
#     "publishable": "pk_test_UUSBZC7h757P649WhX6vrcjM",
#     "secret": "sk_test_38pIcn1zaHZRmqAY7ORNKfgP"
#   },
#   "metadata": {},
#   "object": "account",
#   "payouts_enabled": false,
#   "statement_descriptor": "",
#   "support_email": null,
#   "support_phone": null,
#   "timezone": "Etc/UTC",
#   "type": "standard"
# }

# id	"acct_1BPjEKJesgARHm7l"
# object	"account"
# business_logo	null
# business_name	null
# business_url	null
# charges_enabled	true
# country	"US"
# default_currency	"usd"
# details_submitted	false
# display_name	null
# email	"sunil@chabda.com"
# keys
# secret	"sk_test_OsmOpYD5ykUBmlkAdHsy8cxK"
# publishable	"pk_test_gISpUWe4xOdbebEVXvYyCjgK"
# metadata	{}
# payouts_enabled	false
# statement_descriptor	""
# support_email	null
# support_phone	null
# timezone	"Etc/UTC"
# type	"standard"
