```python
import hashlib
from user_subscription.payment_methods import PaymentDataSchema

def secureTransaction(payment_data):
    """
    Function to secure transaction by hashing sensitive data
    """
    sensitive_data = payment_data['card_number'] + payment_data['expiry_date'] + payment_data['cvv']
    hashed_data = hashlib.sha256(sensitive_data.encode()).hexdigest()
    return hashed_data

def processPayment(payment_data):
    """
    Function to process payment and ensure transaction security
    """
    # Ensure transaction security
    hashed_data = secureTransaction(payment_data)

    # Process payment with hashed data
    # This is a placeholder for actual payment processing code
    payment_status = True  # Placeholder for actual payment status

    if payment_status:
        return 'paymentSuccess'
    else:
        return 'transactionFailure'
```