from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("Bruteforce...")
    attempts = 0
    
    #Open Zip
    with ZipFile('file.zip') as zf:
        with open('rockyou.txt', 'rb') as f: 
    
            #Iterate rockyou.txt
            for p in f:
                password = p.strip()
                attempts += 1
                
                #prints every 1000 attempts
                if attempts % 1000 == 0:
                    print(f"[*] Tried {attempts} passwords...")
                
                #Password Found
                if attempt_extract(zf, password):
                    print(f"PWN: {password.decode()}")
                    exit(0)
    print("Oh No..")

if __name__ == "__main__":
    main()