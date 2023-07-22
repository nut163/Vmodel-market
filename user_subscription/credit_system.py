```python
import datetime
from payment_methods import processPayment
from transaction_security import secureTransaction

class CreditSystem:
    def __init__(self, user_data, payment_data):
        self.user_data = user_data
        self.payment_data = payment_data

    def subscribeUser(self, user_id, payment_method, currency):
        user = self.user_data.get(user_id)
        if not user:
            return 'User not found'
        
        payment_info = self.payment_data.get(payment_method)
        if not payment_info:
            return 'Payment method not supported'
        
        transaction_details = {
            'user_id': user_id,
            'payment_method': payment_method,
            'currency': currency,
            'amount': payment_info['subscription_fee'],
            'date': datetime.datetime.now()
        }
        
        if not secureTransaction(transaction_details):
            return 'Transaction failed'
        
        processPayment(transaction_details)
        
        user['subscription_status'] = 'active'
        user['credit_balance'] += payment_info['subscription_credits']
        
        self.user_data.update(user_id, user)
        
        return 'Subscription successful'

    def addCredits(self, user_id, payment_method, currency, amount):
        user = self.user_data.get(user_id)
        if not user:
            return 'User not found'
        
        payment_info = self.payment_data.get(payment_method)
        if not payment_info:
            return 'Payment method not supported'
        
        transaction_details = {
            'user_id': user_id,
            'payment_method': payment_method,
            'currency': currency,
            'amount': amount,
            'date': datetime.datetime.now()
        }
        
        if not secureTransaction(transaction_details):
            return 'Transaction failed'
        
        processPayment(transaction_details)
        
        user['credit_balance'] += amount
        
        self.user_data.update(user_id, user)
        
        return 'Credits added successfully'
```