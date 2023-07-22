```python
import requests
from user_data_schema import User
from voice_model_data_schema import VoiceModel

def publishTrack(user: User, voice_model: VoiceModel, track_data):
    """
    Function to publish a track to various networks
    """
    # Check if user is a vocalist and has uploaded a voice model
    if user.role != 'vocalist' or not voice_model:
        return {'status': 'error', 'message': 'Only vocalists can publish tracks'}

    # Check if track data is valid
    if not track_data:
        return {'status': 'error', 'message': 'Invalid track data'}

    # Publish track to various networks
    # This is a placeholder for actual publishing code
    # In a real-world application, this would involve API calls to various music distribution networks
    for network in ['Network1', 'Network2', 'Network3']:
        response = requests.post(f'https://{network}.com/publish', data=track_data)

        if response.status_code != 200:
            return {'status': 'error', 'message': f'Failed to publish track to {network}'}

    # If track is successfully published to all networks, send a success message
    return {'status': 'success', 'message': 'Track published successfully'}

def trackPublishSuccess(user: User, voice_model: VoiceModel):
    """
    Function to handle successful track publishing
    """
    # Update user's published tracks
    user.published_tracks.append(voice_model)

    # Send a success message
    return {'status': 'success', 'message': 'Track published successfully, royalties will be calculated when track is used'}
```