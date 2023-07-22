```python
import json
from user_data_schema import UserData
from voice_model_data_schema import VoiceModelData

def displayPurchaseHistory(user_id):
    user_data = UserData.objects.get(id=user_id)
    purchase_history = user_data.purchase_history

    print("Purchase History:")
    for purchase in purchase_history:
        voice_model = VoiceModelData.objects.get(id=purchase.voice_model_id)
        print(f"Voice Model: {voice_model.name}, Price: {purchase.price}, Date: {purchase.date}")

def updatePurchaseHistory(user_id, voice_model_id, price, date):
    user_data = UserData.objects.get(id=user_id)
    purchase_history = user_data.purchase_history
    new_purchase = {
        "voice_model_id": voice_model_id,
        "price": price,
        "date": date
    }
    purchase_history.append(new_purchase)
    user_data.purchase_history = purchase_history
    user_data.save()

def getPurchaseHistory(user_id):
    user_data = UserData.objects.get(id=user_id)
    return json.dumps(user_data.purchase_history)
```