import hashlib
import time



# hashing using sha256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
        

def password_cracker(target_hash, start_time):
    
    #a counter for checking amount of hashes checked
    count = 0 
    
    # opening the file and looping through
    with open("rockyou_2025_00.txt", "r", encoding="utf-8", errors="ignore")as file:
        for line in  file:
            # clean the data by striping any unwanted space or sign befor or after passwords
            password = line.strip()
            # count attempts for performance measurement
            count += 1
            if count % 50000 == 0:
                elapsed = time.time() - start_time
                speed = count / elapsed if elapsed > 0 else 0
                print(f"[+] Tried {count} | Speed: {speed:.2f} p/s")


            # checking validation and returning the outcome
            if hash_password(password) == target_hash:
                return True, password , count
            
        #in case no match found
        return False, None , count
    

#main function / timer and output printing
def main():
    # timer start
    start = time.time()

    target_password = "melnina"
    target_hash = hash_password(target_password)


    #store function to cach outputs
    result = password_cracker(target_hash, start)

    #unpack result's output
    condition, password , count = result
    # timer end
    end = time.time()

    #performance calculation and edge case 0 division
    duration = end -start
    speed = count / duration if duration > 0 else 0
    
    # if password found
    if condition:
        
        print("="*50)
        print(f"password found : {password}")
        print(f"Tried {count} passwords in {duration:.2f} seconds")
        print(f"speed: {speed:.2f} passwords/sec")
        print("="*50)
       
    #if password not found
    else:
        
        print("="*50)
        print("password not found")
        print(f"Tried {count} passwords in {duration:.2f} seconds")
        print(f"speed: {speed:.2f} passwords/sec")
        print("="*50)
       
main()