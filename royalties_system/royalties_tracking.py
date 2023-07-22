```python
import datetime
from user_data_schema import UserData
from voice_model_data_schema import VoiceModelData

class RoyaltiesTracking:
    def __init__(self):
        self.royalties_data = {}

    def track_royalties(self, user: UserData, voice_model: VoiceModelData, usage_count: int):
        user_id = user.user_id
        voice_model_id = voice_model.voice_model_id

        if user_id not in self.royalties_data:
            self.royalties_data[user_id] = {}

        if voice_model_id not in self.royalties_data[user_id]:
            self.royalties_data[user_id][voice_model_id] = {
                'total_usage': 0,
                'total_royalties': 0.0,
                'last_updated': datetime.datetime.now()
            }

        self.royalties_data[user_id][voice_model_id]['total_usage'] += usage_count
        self.royalties_data[user_id][voice_model_id]['total_royalties'] += usage_count * voice_model.price
        self.royalties_data[user_id][voice_model_id]['last_updated'] = datetime.datetime.now()

    def get_royalties(self, user_id: str, voice_model_id: str):
        if user_id in self.royalties_data and voice_model_id in self.royalties_data[user_id]:
            return self.royalties_data[user_id][voice_model_id]
        else:
            return None
```