import hashlib
import time
from dictionary_cracker import load_passwords
from brute_force import generate_passwords

# hashing using sha256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def crack(password_source, target_hash):
    count = 0
    start_time = time.time()


    for password in password_source:
        count +=1

        
        if count % 50000 == 0:
            elapsed = time.time() - start_time
            speed = count / elapsed if elapsed > 0 else 0
            print(f"[+] Tried {count} | Speed: {speed:.2f} p/s")


            
        if hash_password(password) == target_hash:
            return True, password , count
            
    #in case no match found
    return False, None , count


#main function / timer and output printing
def main():
    # timer start
    start = time.time()

    target_password = "weebee@16"
    target_hash = hash_password(target_password)
    
    #choosing cracking method:
    passwords = load_passwords("rockyou_2025_00.txt")
    #or 
    # passwords =generate_passwords("0123456789", 4)

    #store function to cach outputs
    result = crack(passwords, target_hash)

    #unpack result's output
    condition, password , count = result
    # timer end
    end = time.time()

    #performance calculation and edge case 0 division
    duration = end -start
    speed = count / duration if duration > 0 else 0
    
    # if password found
    if condition:
        print(f"password found : {password}")
    #if password not found
    else:
        print("password not found")

    print(f"Tried {count} passwords in {duration:.2f} seconds")
    print(f"speed: {speed:.2f} passwords/sec")

    
main()