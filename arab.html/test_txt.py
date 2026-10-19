import os

DATABASE_FILE = "users.txt"

def save_credential_txt(username: str, password: str):
    """Appends username:password to a plain text file."""
    with open(DATABASE_FILE, 'a') as f:
        f.write(f"{username}:{password}\n")

def check_credential_txt(username: str, password: str) -> bool:
    """Reads the text file line by line to verify credentials."""
    if not os.path.exists(DATABASE_FILE):
        return False

    with open(DATABASE_FILE, 'r') as f:
        for line in f:
            if ":" in line:
                stored_user, stored_pass = line.strip().split(":", 1)
                if stored_user == username and stored_pass == password:
                    return True
    return False

# --- Run Tests ---
if __name__ == "__main__":
    # Clean up old test file if it exists so we start fresh
    if os.path.exists(DATABASE_FILE):
        os.remove(DATABASE_FILE)

    print("1. Registering user 'testuser' with password 'mypass123'...")
    save_credential_txt("testuser", "mypass123")

    print("2. Testing login with CORRECT password...")
    if check_credential_txt("testuser", "mypass123"):
        print("   -> Result: SUCCESS (Logged in!)")
    else:
        print("   -> Result: FAILED (Should have worked)")

    print("3. Testing login with INCORRECT password...")
    if check_credential_txt("testuser", "wrongpassword"):
        print("   -> Result: SUCCESS (Should not have worked)")
    else:
        print("   -> Result: FAILED (Correctly blocked!)")