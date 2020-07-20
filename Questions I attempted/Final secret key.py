import base64

#The encrypted key
message='EUYAHgIRBB1dV1RbSkYUGQQTFUkCUFMCBQ0fDgAVFAsJUE5BTQQAHwQXDAtKV1hBTQQVDQ4AFR0J UE5BTQgdCBMXBQdMHBFGRkFUCgIaCAtYFRkEBBVUS1tSRhtAHBsCAQQXTE1SRhxPEhYIHhJUS1tS Rh1PFhFGRkFUDQ4dRk4UUFMWAw9STBw='

#Your Google username
key='jaskaran.pta'

decrypted_message=[]

#decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

#XOR with Username
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

#The encypted message
print("".join(decrypted_message))
