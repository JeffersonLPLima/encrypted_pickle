import cryptography
from cryptography.fernet import Fernet
import pickle

original_data = {
    'name': "jhon",
    'age' : 23,
    'phone': '55 1182-9119'
}


#save pickle sample
pickle.dump(original_data, open("original_data.pickle", "wb"))


key = Fernet.generate_key()
#write generated key
file = open('original_data.key', 'wb')
file.write(key)
file.close()


#load generated key
file = open('original_data.key', 'rb')
key  = file.read()
file.close()


#load pickle sample
data = pickle.load(open("original_data.pickle", "rb"))
data = pickle.dumps(data) #get bytes formart

fernet = Fernet(key)
encrypted = fernet.encrypt(data) #encrypt data bytes

print(f'Encrypted data:{encrypted}')
file = open('encrypted_data.pickle', 'wb')
file.write(encrypted)
file.close()


decrypted = pickle.loads(fernet.decrypt(encrypted)) #loads (load string-byte format) decripted data
print(f'Decrypted data:{decrypted}')