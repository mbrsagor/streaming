import firebase_admin
from firebase_admin import credentials, messaging


cred = credentials.Certificate("service-key.json")
firebase_admin.initialize_app(cred)

def send_push(title, msg, registration_token, dataObject=None):
    try:
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=msg,
            ),
            data=dataObject,
            tokens=registration_token,
        )

        response = messaging.send_multicast(message)
    except messaging.QuotaExceededError:
        raise f'Exceeding FCM notifications quota'
