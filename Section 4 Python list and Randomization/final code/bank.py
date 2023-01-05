all_users = ["john", "luke", "philip"]

def register_user(name, id):
    all_users.append(name)

def delete_user(name):
    all_users.remove(name)

def total_user():
    return len(all_users)