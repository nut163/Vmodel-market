```python
import os
from user_data_schema import User
from voice_model_data_schema import VoiceModel

def uploadVoiceModel(user_id, voice_model_file):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404

    if not voice_model_file:
        return {"message": "No voice model file provided"}, 400

    if not voice_model_file.filename.endswith('.vm'):
        return {"message": "Invalid file type. Please upload a .vm file"}, 400

    voice_model = VoiceModel(user_id=user.id)
    voice_model.save()

    file_path = os.path.join('voice_models', str(voice_model.id), voice_model_file.filename)
    voice_model_file.save(file_path)

    voice_model.file_path = file_path
    voice_model.save()

    return {"message": "voiceModelUploadSuccess", "voiceModelId": voice_model.id}, 200
```