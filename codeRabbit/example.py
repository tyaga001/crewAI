import random
from datetime import datetime

class UserManagment:
    def __init__(self)
        self.users = {}

    def add_user(self, username, password):
        if username in self.users
            return False
        self.users[username] = {"password": password, "created_at": datetime.now()}
        return True

    def authenticate(self, username, password):
        if username not in self.users:
            return False
        return self.users[username]["password"] == password

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        return False

def generate_report(users):
    report = f"User Report - Generated on {datetime.now().strftime('%Y-%m-%d')}\n"
    report += "=" * 40 + "\n"
    for username, data in users.items():
        report += f"Username: {username}\n"
        report += f"Created: {data['created_at']}\n"
        report += "-" * 20 + "\n"
    return report

def main():
    user_system = UserManagment()

    # Add some users
    user_system.add_user("alice", "password123")
    user_system.add_user("bob", "qwerty456")
    user_system.add_user("charlie", "secret789")

    # Authenticate users
    print(user_system.authenticate("alice", "password123"))  # Should be True
    print(user_system.authenticate("bob", "wrongpassword"))  # Should be False

    # Generate and print report
    report = generate_report(user_system.users)
    print(report)

    # Delete a user
    user_system.delete_user("bob")

    # Try to authenticate deleted user
    print(user_system.authenticate("bob", "qwerty456"))  # Should be False

if __name__ == "__main__"
    main()