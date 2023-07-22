```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/lyrics_input', methods=['POST'])
def input_lyrics():
    data = request.get_json()
    user_id = data.get('user_id')
    lyrics = data.get('lyrics')

    if not user_id or not lyrics:
        return jsonify({'message': 'Missing user_id or lyrics'}), 400

    # Save the lyrics to the database
    # This is a placeholder and should be replaced with actual database interaction
    lyrics_db = {}
    lyrics_db[user_id] = lyrics

    return jsonify({'message': 'Lyrics input successful', 'lyrics': lyrics}), 200

if __name__ == '__main__':
    app.run(debug=True)
```