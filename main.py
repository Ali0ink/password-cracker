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


    while True:
        print("please choose one from below: ")
        print("1.Dictionary Attack")
        print("2.Brute Force")

        choice = input("your choice: ")

        #choosing cracking method:
        if choice == "1":
            passwords = load_passwords("rockyou_2025_00.txt")
            
        if choice == "2":
            charset = input("Enter charset (e.g 01234): ")
            length = int(input("Enter password length: "))
            passwords =generate_passwords(charset, length)
                
        else:
            print("Invalid input")
            
        target_password = input("Enter a password to hash (for test): ")
        target_hash = hash_password(target_password)
               

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