roles = {
    'admin': ['read','write','delete','manage_users','view_logs'],
    'editor': ['read','write'],
    'viewer': ['read'],
    'guest': [],
    'auditor': ['read','view_logs']   # NEW ROLE
}

users = {
    'alice':'admin',
    'bob':'editor',
    'carol':'viewer',
    'dave':'guest',
    'eve':'auditor'   # NEW USER
}

def check_access(username, permission):
    role = users.get(username, 'guest')
    allowed = permission in roles.get(role, [])
    print(f'{username} ({role}) -> {permission}: {"GRANTED" if allowed else "DENIED"}')
    return allowed

print('--- Access Control Test ---')

for user in ['alice','bob','carol','dave','eve','unknown']:
    for perm in ['read','write','delete','manage_users','view_logs']:
        check_access(user, perm)

print("\n--- Edge Case Tests ---")
check_access('ghost', 'read')
check_access('alice', 'hack_system')
