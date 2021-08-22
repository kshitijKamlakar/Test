from payment_services.models import Payment_Status
from django.apps import AppConfig
from django.views.decorators.csrf import csrf_exempt
from django.apps import AppConfig
from django.http import request, HttpResponse
import stripe
import json
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class PaymentServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payment_services'


class Payment_Details(object):
    def __init__(self,card_number ,card_exp_month,card_exp_year,card_cvv, card_name = None):
        self.card_number = card_number
        self.card_exp_month = card_exp_month
        self.card_exp_year = card_exp_year
        self.card_cvv = card_cvv
        self.card_name = card_name

'''
initialize payment method. Will be called whenever a payment is initiated
input: Json request for subscription
output: Success or failed message
'''
@csrf_exempt
def initialize_payment(request):
    
    api_key = getattr(settings, "STRIVE_API_KEY", None)

    if api_key is None:
        logger.error('Error while reading API key')
        return  HttpResponse(json.dumps({'Status':'Internal Server Error with API key'}), content_type="application/json",status = 503)
    
    stripe.api_key = api_key

    try :
        data = json.loads(request.body)
        payment_Details = Payment_Details(**data)

        payment_method = create_payment_method(payment_Details.card_number,payment_Details.card_exp_month,
                                            payment_Details.card_exp_year,payment_Details.card_cvv)
        customer = create_customer(payment_method)

        _ = update_payment_method(payment_method['id'],customer['id'])
    
        price_object = create_price_object()

        create_subscription(customer['id'],price_object['id'])
        #def __init__(self,id,payment_method,customer_name,sub_status,sub_purchase_data,price, status = None):
        payment_status = Payment_Status('Card',payment_Details.card_name,'success',price_object['id'],'success')
        #payment_status.store_payment_info()

        return HttpResponse(json.dumps({'success':True}), content_type="application/json", status = 200)
    
    except Exception as e:
        logger.error(e)
        payment_status = Payment_Status('Card',payment_Details.card_name,'success',price_object['id'],'Failed')
        #payment_status.store_payment_info()
        return  HttpResponse(json.dumps({'Status':'Internal Server Error'}), content_type="application/json",status = 503)


'''
Generate card object.
Param: card number, card exp month, card exp year, card cvv
output: card id
'''
def generate_card(card_number,card_exp_month,card_exp_year,card_cvv):

    data = stripe.Token.create(
        card={
                "number": str(card_number),
                "exp_month": int(card_exp_month),
                "exp_year": int(card_exp_year) ,
                "cvc": str(card_cvv),
            }
    )
    card_id = data['id']
    return card_id

'''
Create Payment method with given card details
Param: card number, card exp month, card exp year, card cvv
output: card id
'''
def create_payment_method(card_number,card_exp_month,card_exp_year,card_cvv):
    pay_method = stripe.PaymentMethod.create(
    type="card",
    card={
        "number": card_number,
        "exp_month": card_exp_month,
        "exp_year": card_exp_year,
        "cvc": card_cvv,
        },
    )

    return pay_method

'''
Create customer with given payment method
param: payment method json data
output: customer object
'''
def create_customer(pay_method):
    cust = stripe.Customer.create(
            payment_method = pay_method['id'],
            invoice_settings={
            'default_payment_method': pay_method['id'],
            },
            ) 
            
    return cust

'''
Update payment method of payment id to specified customer id
Param: payment id, customer id
output: updated payment method
'''
def update_payment_method(payment_id,customer_id):
    updated_payment_method = stripe.PaymentMethod.attach(payment_id,
                                                        customer = customer_id)
    return updated_payment_method

'''
Create subscription for given product price id and customer
Param: customer id, price id
output: subscription object
'''
def create_subscription(customer_id,price_id):
    sub = stripe.Subscription.create(customer = customer_id,
                        
                        items = [
                            {
                                'price' : price_id,
                            }

                        ])
    return sub


'''
webhook method for subscrition created and subscription updated method.
output: success or failed message
'''
@csrf_exempt
def create_webhook(request):
    payload = request.data
    webhook_secret = 'whsec_r1Mpu4lQ6KVTgw9IIkSawAKntAVDLoea'
    try:
        event = json.loads(payload)
    except Exception as e:
        print('Webhook error while parsing basic request.' + str(e))
        logger.error('Webhook error while parsing basic request.' + str(e))
        return HttpResponse(json.dumps({'Status':'Failed'}), content_type="application/json")
    # Handle the event
    signature = request.headers.get('stripe-signature')
    try:
        event = stripe.Webhook.construct_event(
            payload=request.data, sig_header=signature, secret=webhook_secret)
        data = event['data']
    except Exception as e:
        logger.error(e)
        return HttpResponse(json.dumps({'success':True}), content_type="application/json")
    if event or event['type'] == 'customer.subscription.created':
        payment_intent = event['data']['object']  # contains a stripe.customer.subscription.created
        
    elif event or event['type'] == 'customer.subscription.updated':
        payment_method = event['data']['object']  # contains a scustomer.subscription.updated
        
    else:
        pass
    return HttpResponse(json.dumps({'Status':'Success'}), content_type="application/json")


'''
Method to make payment
Param: card id and payment amount
output: charge object
'''
def make_payment(card_id, payment_amount):
    payment = stripe.Charge.create(
                amount= payment_amount, # convert amount to cents
                currency='inr',
                description='Example charge',
                source=card_id,
    )
    payment_check = payment['paid']    # return True for successfull payment
    return payment_check


'''
Create price object
output: price object
'''
def create_price_object():
    return stripe.Price.create(
    unit_amount=1000,
    currency="inr",
    recurring={"interval": "month"},
    product="prod_K4arBhm6WQH3Sq",
    )
