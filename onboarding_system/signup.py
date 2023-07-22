```python
import hashlib
import os
from user_data_schema import User

def signupUser(username, password, email):
    # Check if user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return {"message": "User already exists"}, 400

    # Create new user
    new_user = User(username=username, email=email)

    # Hash the password for security
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    password_hash = salt + key

    new_user.password_hash = password_hash

    # Save the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {"message": "signupSuccess"}, 200
```