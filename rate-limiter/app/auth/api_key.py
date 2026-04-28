VALID_API_KEYS = {"12345", "abcde"}

def get_user(api_key):
    if api_key in VALID_API_KEYS:
        return api_key
    return None