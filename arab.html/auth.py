import json
import os

DATABASE_FILE = "users_plain.json"

def register_user(username: str, password: str):
    """Registers a new user, saving the password in plaintext."""
    users = {}
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}

    if username in users:
        print(f"Error: User '{username}' already exists.")
        return False

    # Storing the password directly as plaintext
    users[username] = password

    with open(DATABASE_FILE, 'w') as f:
        json.dump(users, f, indent=4)
    
    print(f"Success: User '{username}' registered.")
    return True

def verify_user(username: str, password: str) -> bool:
    """Verifies user credentials by comparing plaintext strings."""
    if not os.path.exists(DATABASE_FILE):
        print("Error: Database file not found.")
        return False

    with open(DATABASE_FILE, 'r') as f:
        users = json.load(f)

    # Check if username exists and password matches exactly
    if username in users and users[username] == password:
        print(f"Success: Welcome back, {username}!")
        return True
    else:
        print("Error: Invalid username or password.")
        return False

# --- Example Usage ---
if __name__ == "__main__":
    # Register user
    register_user("testuser", "asher123z")
    
    # Successful login
    verify_user("testuser", "asher123z")
    
    # Failed login
    verify_user("testuser", "wrongpassword")