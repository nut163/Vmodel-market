```python
import stripe
from user_data_schema import UserData
from payment_data_schema import PaymentData

stripe.api_key = "your_stripe_api_key"

def process_payment(user_id, payment_method_id, amount, currency):
    user = UserData.objects.get(id=user_id)
    payment_data = PaymentData.objects.get(id=payment_method_id)

    if payment_data.method == "stripe":
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency=currency,
                source=payment_data.details,
                description=f"Charge for {user.username}"
            )
            return charge
        except stripe.error.CardError as e:
            print(f"Card error: {e}")
            return None
    else:
        print("Unsupported payment method")
        return None

def add_payment_method(user_id, method, details):
    user = UserData.objects.get(id=user_id)
    payment_data = PaymentData(method=method, details=details)
    payment_data.save()
    user.payment_methods.add(payment_data)
    user.save()

def remove_payment_method(user_id, payment_method_id):
    user = UserData.objects.get(id=user_id)
    payment_data = PaymentData.objects.get(id=payment_method_id)
    user.payment_methods.remove(payment_data)
    user.save()
    payment_data.delete()
```