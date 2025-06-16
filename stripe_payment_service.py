import requests
from django.conf import settings
# Stripe amount converter settings
from utils.stripe_amount_calculator import AmountConverter

# URLS
customer_url = 'https://api.stripe.com/v1/customers'
ephemeral_key_url = 'https://api.stripe.com/v1/ephemeral_keys'
payment_intents_url = 'https://api.stripe.com/v1/payment_intents'
payment_info_url = 'https://api.stripe.com/v1/payment_intents'

# Stripe API key
stripe_api_key = settings.STRIPE_SECRET_KEY

# This header will be used for global.
headers = {
    'Authorization': f'Bearer {stripe_api_key}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
headers_with_stripe_version = {
    'Authorization': f'Bearer {stripe_api_key}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Stripe-Version': '2022-08-01'
}


def make_stripe_payment(name, email, phone, amount, currency):
    """
    Name: Send payment data to the customer.
    Description: Requested customer user information sent to the Stripe customer API.
    :param currency:
    :param amount:
    :param name:
    :param email:
    :param phone:
    :return:
    method: POST request
    """

    data = {
        'name': name,
        'email': email,
        'phone': phone,
    }
    response = requests.post(customer_url, headers=headers, data=data)
    customer_id = response.json()['id']
    # set customer ephemeral keys
    customer_data = {
        'customer': customer_id
    }
    ephemeral_response = requests.post(ephemeral_key_url, headers=headers_with_stripe_version, data=customer_data)
    # Set payment intent
    converter = AmountConverter() # convert dolor to cents
    intent_data = {
        'customer': customer_id,
        'amount': converter.to_cents(amount),
        'currency': currency,
    }

    intent_response = requests.post(payment_intents_url, headers=headers, data=intent_data)
    intent_id = intent_response.json()['id']
    client_secret = intent_response.json()['client_secret']
    ephemeral_secret_key = ephemeral_response.json()['secret']
    # Final response
    final_response = {
        'intent_id': intent_id,
        'client_secret': client_secret,
        'ephemeral_secret_key': ephemeral_secret_key,
    }
    return final_response


def set_customer_ephemeral_key(customer):
    """
    Name: Set customer ephemeral keys.
    :param customer:
    :return:
    Method: POST request
    """
    data = {
        'customer': customer
    }
    response = requests.post(ephemeral_key_url, headers=headers_with_stripe_version, data=data)
    return response.text


def set_payment_intent(customer, amount, currency):
    """
    Name: Payment intent
    :param customer:
    :param amount:
    :param currency:
    :return:
    """

    data = {
        'customer': customer,
        'amount': amount,
        'currency': currency
    }
    response = requests.post(payment_intents_url, headers=headers, data=data)
    return response.text


def get_payment_information(payment_intent_id):
    """
    Name: Get payment information.
    :return: payment_intent_id
    """
    url = f"{payment_info_url}/{payment_intent_id}"
    payment_response = requests.get(url, headers=headers)
    response = {
        'id': payment_response.json()['id'],
        'object': payment_response.json()['object'],
        'amount': payment_response.json()['amount'],
        'currency': payment_response.json()['currency'],
        'customer': payment_response.json()['customer'],
        'client_secret': payment_response.json()['client_secret'],
        'confirmation_method': payment_response.json()['confirmation_method'],
        'payment_method_types': payment_response.json()['payment_method_types'],
        'balance_transaction': payment_response.json()['charges']['data'][0]['balance_transaction'],
        'card_brand_name': payment_response.json()['charges']['data'][0]['payment_method_details']['card']['brand'],
        'payment_from_country': payment_response.json()['charges']['data'][0]['payment_method_details']['card'][
            'country'],
    }
    return response
