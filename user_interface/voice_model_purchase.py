```python
import tkinter as tk
from user_subscription import credit_system, payment_methods
from royalties_system import royalties_calculation

class VoiceModelPurchase(tk.Frame):
    def __init__(self, parent, user_data, voice_model_data):
        tk.Frame.__init__(self, parent)
        self.user_data = user_data
        self.voice_model_data = voice_model_data
        self.purchase_button = tk.Button(self, text="Purchase", command=self.purchase_voice_model)
        self.purchase_button.pack()

    def purchase_voice_model(self):
        selected_voice_model = self.voice_model_data.get_selected_model()
        if not selected_voice_model:
            print("No voice model selected.")
            return

        if self.user_data['credit_balance'] < selected_voice_model['price']:
            print("Insufficient credit balance.")
            return

        payment_success = payment_methods.process_payment(self.user_data, selected_voice_model['price'])
        if not payment_success:
            print("Payment failed.")
            return

        self.user_data['credit_balance'] -= selected_voice_model['price']
        self.user_data['purchase_history'].append(selected_voice_model)
        royalties_calculation.calculate_royalties(selected_voice_model)

        print("Voice model purchase successful.")
```