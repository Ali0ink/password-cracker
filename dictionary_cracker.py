
def load_passwords(file_path):
    
    # opening the file 
    with open(file_path, "r", encoding="utf-8", errors="ignore")as file:
        for line in  file:
            yield line.strip()
    

