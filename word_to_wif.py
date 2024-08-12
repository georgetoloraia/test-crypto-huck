# import hashlib
# from bit import Key
# import csv

# def text_to_sha256(text):
#     return hashlib.sha256(text.encode('utf-8')).hexdigest()

# def sha256_to_wif(sha256_hex):
#     key = Key.from_hex(sha256_hex)
#     return key.to_wif()

# def convert_text_to_wif_and_save(input_file, output_file):
#     with open(input_file, 'r') as file:
#         text = file.read().strip()

#     sha256_hex = text_to_sha256(text)
#     wif_compressed = sha256_to_wif(sha256_hex)

#     with open(output_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([wif_compressed])
    
#     print(f"WIF compressed private key generated from text in '{input_file}' and saved to '{output_file}'")

# # Example usage
# convert_text_to_wif_and_save('compressed_wifs.csv', 'compressed_wifsss.csv')

import hashlib
from bit import Key
import csv
import base58

def text_to_sha256(text):
    """Convert text to SHA256 hex."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def sha256_to_wif(sha256_hex):
    """Convert SHA256 hex to WIF."""
    # key = Key.from_hex(sha256_hex)
    # return key.to_wif()  # Only return compressed WIF
    key = Key.from_hex(sha256_hex)
    
    # Compressed WIF
    wif_compressed = key.to_wif()
    
    # Uncompressed WIF
    # Convert the SHA256 hex to bytes
    private_key_bytes = bytes.fromhex(sha256_hex)
    
    # Create WIF for uncompressed format manually
    # Add 0x80 prefix for mainnet
    prefix = b'\x80'
    # Add the private key bytes
    key_with_prefix = prefix + private_key_bytes
    # Double SHA256 hash to calculate checksum
    checksum = hashlib.sha256(hashlib.sha256(key_with_prefix).digest()).digest()[:4]
    # Concatenate key with checksum
    wif_uncompressed_bytes = key_with_prefix + checksum
    # Encode in base58
    wif_uncompressed = base58.b58encode(wif_uncompressed_bytes).decode('utf-8')

    return wif_compressed, wif_uncompressed



def convert_text_to_wif_and_save(input_file, output_file):
    """Read text from CSV, convert to WIF, and save results to a new CSV."""
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the header
        # writer.writerow(['Text', 'SHA256', 'WIF Compressed'])
        
        for row in reader:
            if row:  # Check if the row is not empty
                text = row[0].strip()
                sha256_hex = text_to_sha256(text)
                wif_compressed, wif_uncompres  = sha256_to_wif(sha256_hex)
                writer.writerow([wif_compressed + "\n" + wif_uncompres])
                # print(f"{wif_compressed}")

    print(f"Results saved to '{output_file}'")

# Example usage
convert_text_to_wif_and_save('word.txt', 'privs.txt')
