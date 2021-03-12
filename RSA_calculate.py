from random import randrange # select a random E
import miller_rabin as miller 

'''
Generate The Random Number E
'''
def generate_E(totient_of_N):

    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = randrange(2,totient_of_N) 
        if(mdc(totient_of_N,e) == 1): #Coprimos
            return e

'''
Cipher The Plain Text using Public Key
'''
def cipher(words,e,n): # get the words and compute the cipher

    lista = []
    encrypted = ''
    for letter in words:
        k = ord(letter)
        k = k**e
        d = k % n
        lista.append(d)

    for letter_cipher in lista:
        aux = chr(letter_cipher)
        encrypted += aux

    return encrypted

'''
Decipher The Plain Text Private Key
'''
def decipher(cifra,n,d):
    lista = []
    text_original = ''
    for letter in cifra:
        result = (ord(letter))**d
        plain_text = result % n
        letter_of_text = chr(plain_text)
        lista.append(letter_of_text)
    

    for letter_of_text in lista:
        text_original += letter_of_text

    return text_original

'''
Compute The Private Key
'''
def calculate_private_key(toti,e):
    d = 1
    while(((d*e) % toti) != 1):
        d += 1
    return d


if __name__=='__main__':
    
    while(True):
        p = int(input("Number P: ")) #Prime 1
        q = int(input("Number Q: ")) #Prime 2
        if (miller.isPrime(p) and miller.isPrime(q)):
            break
        else:
            print("P and Q must be primes! Please try again...") 

           
    text = input("Insert message: ")
    
    n = p*q # N number

    totient_of_N = (p-1)*(q-1) # Phi number φ(x)

    e = generate_E(totient_of_N) # generate E

    public_key = (n, e)
    print('Your public keys:', public_key)

    text_cipher = cipher(text,e,n)
    print('Your encrypted message:', text_cipher)

    d = calculate_private_key(totient_of_N,e)
    print('Your private key is:', d)

    original_text = decipher(text_cipher,n,d)
    print('your original message:', original_text)