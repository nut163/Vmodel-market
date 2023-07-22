```python
import os
from pydub import AudioSegment
from pydub.playback import play

# Importing shared dependencies
from user_data_schema import User
from voice_model_data_schema import VoiceModel

def generatePreview(user_id, voice_model_id, lyrics):
    user = User.query.get(user_id)
    voice_model = VoiceModel.query.get(voice_model_id)

    if user and voice_model:
        # Assuming the voice model files are stored in a directory named 'voice_models'
        voice_model_file = os.path.join('voice_models', voice_model.file_name)

        # Load voice model
        voice = AudioSegment.from_file(voice_model_file)

        # Generate preview (3-5 seconds)
        preview = voice[:5000]

        # Assuming the lyrics are in a text file
        with open(lyrics, 'r') as file:
            lyrics_text = file.read()

        # Play the preview
        play(preview)

        # Send a message to the user interface
        message = {
            'name': 'previewGenerated',
            'data': {
                'user_id': user.id,
                'voice_model_id': voice_model.id,
                'preview': preview,
                'lyrics': lyrics_text
            }
        }

        return message

    else:
        return {'error': 'User or Voice Model not found'}
```