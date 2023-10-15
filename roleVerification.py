# Define roles and their permissions
roles = {
    "admin": ["create", "read", "update", "delete"],
    "user": ["read"],
    "guest": []
}

# Simulate user authentication (you may replace this with your authentication logic)
def authenticate_user(username):
    # For the sake of this example, we're using a simple dictionary as a user database
    users = {
        "admin_user": "admin",
        "regular_user": "user",
        "guest_user": "guest"
    }
    return users.get(username, "guest")  # Default to guest role if the user is not found

# Example user
username = "admin_user"
user_role = authenticate_user(username)

# Check user's role
if user_role in roles:
    print(f"{username} has the following permissions: {roles[user_role]}")
else:
    print(f"{username} has an unknown role")

# Check specific permission
if "create" in roles[user_role]:
    print(f"{username} can create.")
else:
    print(f"{username} cannot create.")
