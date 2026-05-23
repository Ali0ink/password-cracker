import hashlib
import time


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
        

def password_cracker(target_hash):
    
    count = 0
    with open("rockyou_2025_00.txt", "r", encoding="utf-8", errors="ignore")as file:

        for line in file:
            password = line.strip()
            count += 1
            if hash_password(password) == target_hash:
                return True, password , count
        
        return False, None , count
def main():
    start = time.time()

    result = password_cracker(hash_password("mmmmmvvvvvvvvvvvvvvvv"))

    condition, password , count = result
    end = time.time()

    duration = end -start
    speed = count / duration


    if condition:
        
        print("="*50)
        print(f"password found : {password}")
        print(f"Tried {count} passwords in {duration:.2f} seconds")
        print(f"speed: {speed:.2f} passwords/sec")
        print("="*50)
    else:
        
        print("="*50)
        print("password not found")
        print(f"Tried {count} passwords in {duration:.2f} seconds")
        print(f"speed: {speed:.2f} passwords/sec")
        print("="*50)

main()