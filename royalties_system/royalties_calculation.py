```python
import datetime
from user_subscription.credit_system import User
from onboarding_system.upload_voice_models import VoiceModel

class Royalties:
    def __init__(self, user: User, voice_model: VoiceModel):
        self.user = user
        self.voice_model = voice_model
        self.royalties = 0

    def calculate_royalties(self, usage_count: int):
        royalty_rate = 0.10  # 10% royalty rate
        self.royalties += usage_count * self.voice_model.price * royalty_rate
        return self.royalties

    def update_user_balance(self):
        self.user.credit_balance += self.royalties
        self.user.purchase_history.append({
            'date': datetime.datetime.now(),
            'description': f'Royalties from {self.voice_model.vocalist}',
            'amount': self.royalties
        })
        self.royalties = 0

    def calculate_and_update(self, usage_count: int):
        self.calculate_royalties(usage_count)
        self.update_user_balance()
```