import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_file():
    
        return file.readlines()
        

def password_cracker(target_hash):
    with open("rockyou_2025_00.txt", "r", encoding="utf-8", errors="ignore")as file:

        for line in file:
            password = line.strip()

            if hash_password(password) == target_hash:
                print(f"["+("="*50)+"]")
                print(f"password found: {password}")
                print(f"["+("="*50)+"]")
                return password
        print("password not found")

password_cracker(hash_password("1234"))