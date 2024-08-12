# import requests

# def get_bitcoin_balance(address):
#     url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an error for bad responses
#         data = response.json()
#         balance = data['balance'] / 1e8  # Convert from satoshi to bitcoin
#         return balance
#     except requests.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return None

# # Bitcoin address to check
# address = "18xAigFJeWCuUuPcBcYHN8DreuGzmruvvs"
# balance = get_bitcoin_balance(address)

# if balance is not None:
#     print(f"Balance for {address}: {balance} BTC")
# else:
#     print("Could not fetch balance.")




'''
========================================================
'''

import os
import hashlib
import binascii
import base58
import ecdsa
import requests
from Crypto.Hash import RIPEMD160

def generate_private_key():
    """Generate a random 256-bit private key"""
    # return binascii.hexlify(os.urandom(32)).decode('utf-8')
    # return "bbed47de967bd9eb76ec1c6fbcf50bd99b0bae4a517585c3a52b219b4f02dd07"
    return "aaee55cccff2d259e0b666e2360f9d48f1948f06a9b5b79d11ce1289fc4938fc"
    # return "19bdb154544739fe4d43b6e169510480dace5bf491e86df14a0451c7577a425e"

def private_to_public(private_key):
    """Convert the private key to a public key"""
    private_key_bytes = binascii.unhexlify(private_key)
    print(f"{private_key}\n")
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return '04' + binascii.hexlify(vk.to_string()).decode('utf-8')


def public_to_address(public_key):
    """Convert the public key to a Bitcoin address using pycryptodome for RIPEMD-160."""
    output = hashlib.sha256(binascii.unhexlify(public_key)).digest()
    # Using RIPEMD160 from pycryptodome
    ripemd160 = RIPEMD160.new()
    ripemd160.update(output)
    output = ripemd160.digest()
    address = b'\x00' + output  # Append 0x00 in front of the RIPEMD-160 hash
    checksum = hashlib.sha256(hashlib.sha256(address).digest()).digest()[:4]
    address += checksum
    return base58.b58encode(address).decode('utf-8')


# def public_to_address(public_key):
#     """Convert the public key to a Bitcoin address"""
#     output = hashlib.sha256(binascii.unhexlify(public_key)).digest()
#     output = hashlib.new('ripemd160', output).digest()
#     address = b'\x00' + output  # Append 0x00 in front of the RIPEMD-160 hash
#     checksum = hashlib.sha256(hashlib.sha256(address).digest()).digest()[:4]
#     address += checksum
#     return base58.b58encode(address).decode('utf-8')

def get_bitcoin_balance(address):
    """Fetch the Bitcoin balance for the given address using the BlockCypher API"""
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        balance = data['balance'] / 1e8  # Convert from satoshi to bitcoin
        return balance
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Generate a new Bitcoin address
private_key = generate_private_key()
public_key = private_to_public(private_key)
address = public_to_address(public_key)

print(f"Generated Bitcoin address: {address}")

# Fetch and print the balance of the generated address
balance = get_bitcoin_balance(address)
if balance is not None:
    print(f"Balance for {address}: {balance} BTC")
else:
    print("Could not fetch balance or address has no transactions.")
