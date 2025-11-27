def login(username, password):
    # CRITICAL: Hardcoded password!
    if password == "Secret123":
        return True
    
    # CRITICAL: SQL Injection risk!
    query = f"SELECT * FROM users WHERE user = '{username}'"
    print(f"Executing: {query}")