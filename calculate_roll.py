import hmac
import hashlib

def calculate_roll(server_seed, client_seed, nonce):
    # Create the two strings as described
    string1 = f"{nonce}:{server_seed}:{nonce}"
    string2 = f"{nonce}:{client_seed}:{nonce}"
    
    # Use HMAC-SHA512 to hash string1 with string2 as the key
    hash_hex = hmac.new(string2.encode(), string1.encode(), hashlib.sha512).hexdigest()
    
    # Take the first 8 characters of the hex string and convert to decimal
    first_eight_decimal = int(hash_hex[:8], 16)
    
    # Divide the decimal by 429496.7295 and round to the nearest whole number
    roll = round(first_eight_decimal / 429496.7295)
    
    # Ensure the roll is within the maximum possible value
    roll = min(roll, 10000)
    
    return roll

# Example usage
server_seed = "0000000000000000000000000000000000000000000000000000000000000000"
client_seed = "LGp6hCqsYz8cfaWr"
nonce = 130234

rolled_number = calculate_roll(server_seed, client_seed, nonce)
print("Calculated rolled number:", rolled_number)
