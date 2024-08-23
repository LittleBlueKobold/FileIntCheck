import hashlib  # import module

def get_file_hash(file_path, hash_algorithm='sha256'):  #define hashing algorithm
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

file_path = "important_file.txt"  #file to open/file path
print(f"File Hash: {get_file_hash(file_path)}")
