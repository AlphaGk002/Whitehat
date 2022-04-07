import whitehat

# Encrypt
encrypt = whitehat.Cryptography.CaesarCipher.encrypt(input("Enter the String:"))
print("It is encrypt:", encrypt)
decrypt = whitehat.Cryptography.CaesarCipher.decrypt(cipher=encrypt)
print("It is decrypt:", decrypt)

# Decrypt
decrypt1 = whitehat.Cryptography.CaesarCipher.decrypt(cipher=(input("\nEnter the encrypt value:")))
print("It is decrypt:", decrypt1)


# Output
"""
1.Encrypt :
        --> Enter the String in 'python'
output  -->It is Encrypt : ravjqp

2.Decrypt:
        -->Enter the Encrypt value:ravjqp
      
output  -->It is Decrypt :python      
"""
