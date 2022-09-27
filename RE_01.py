#Hash Cracker
import hashlib
'''
string1 = "abc1234"

hash1 = hashlib.md5(string1.encode('utf-8')).hexdigest()
hash2 = hashlib.sha1(string1.encode('utf-8')).hexdigest()

nhash = hashlib.new('md4', string1.encode('utf-16le')).hexdigest().upper()

print(hash1)
print(hash2)
'''

hash_type = input("Enter the hash type\n1 md5\n2 sha1\n3 NTLM\n")
path_to_wordlist = input ("Enter path to word list\n")
input_hash = input("Enter the hash t crach\n")

def md5_crack(hash_to_crack, path_to_wordlist):
    c =1 
    with open(path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n','').rstrip()
            hash_current = hashlib.md5(current_pass.encode('utf-8')).hexdigest() 
            c +=1 

            if c%100000 == 0:
                print(f"Done {c} passwords current --> {current_pass}")
            if hash_current == hash_to_crack:
                print("Password found: " + current_pass)
                break


def sh1_crack(hash_to_crack, path_to_wordlist):
    c =1 
    with open(path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n','').rstrip()
            hash_current = hashlib.new('md4',current_pass.encode('utf-16le')).hexdigest().upper() 
            c +=1

            if c%100000 == 0:
                print(f"Done {c} passwords current --> {current_pass}")
            if hash_current == hash_to_crack:
                print("Password found: " + current_pass)
                break


if hash_type == "1":
    md5_crack(input_hash, path_to_wordlist)   
elif hash_type == "2":
    sh1_crack(input_hash, path_to_wordlist)
