#!/usr/bin/env python3

# Homework Number: 01
# Name: Nazran Farook
# ECN Login: nfarook
# Due Date: 01/20/2022

from BitVector import *

def cryptBreak(ciphertextFile, key_bv):
    # Arguments:
    # * ciphertextFile: String containing file name of the ciphertext
    # * key_bv: 16-bit BitVector for the decryption key
    #
    # Function Description:
    # Attempts to decrypt the ciphertext within ciphertextFile file using
    # key_bv and returns the original plaintext as a string

    # Set the pass phrase
    PassPhrase = "Hopes and dreams of a million years" 

    # Set the blocksize to 16
    BLOCKSIZE = 16
    numbytes = BLOCKSIZE // 8 

    # Reduce the passphrase to a bit array of size BLOCKSIZE:
    # and thus obtain the initial vector
    bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)             
    for i in range(0,len(PassPhrase) // numbytes):         
        textstr = PassPhrase[i*numbytes:(i+1)*numbytes]                         
        bv_iv ^= BitVector( textstring = textstr ) 

    # Create a bitvector from the ciphertext hex string:
    FILEIN = open(ciphertextFile)
    encrypted_bv = BitVector( hexstring = FILEIN.read() )

    # Create a bitvector for storing the decrypted plaintext bit array:
    msg_decrypted_bv = BitVector( size = 0 )

    # Carry out differential XORing of bit blocks and decryption:
    previous_decrypted_block = bv_iv                       
    for i in range(0, len(encrypted_bv) // BLOCKSIZE):     
        bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]     
        temp = bv.deep_copy()                              
        bv ^=  previous_decrypted_block                    
        previous_decrypted_block = temp                    
        bv ^=  key_bv                                      
        msg_decrypted_bv += bv                             

    # Extract plaintext from the decrypted bitvector:    
    outputtext = msg_decrypted_bv.get_text_from_bitvector()

    return outputtext

if __name__ == '__main__':

    # For true brute force attack, the complete range would be range(2**16)
    # But it takes a lot of time, hence putting a small range which
    # contains the actual key
    for intValue in range(29500, 30000):

        # Create a key vector from integer value
        key_bv = BitVector(intVal=intValue, size=16)

        # Use the cryptBreak function to obtain message for this key
        decryptedMessage = cryptBreak('ciphertext.txt', key_bv)

        # Check if it was correct key
        if 'Douglas Adams' in decryptedMessage:
            print('Encryption Broken!')
            print('intValue:', intValue)
            print('Decrypted message:', decryptedMessage)
            break
        
    print("Test complete.")