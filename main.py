import numpy as np


alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def matrix_mod_inv(key, modulus):
    det = int(np.round(np.linalg.det(key)))
    det_inv = det % modulus
    matrix_modulus_inv = det_inv * np.round(det*np.linalg.inv(key)).astype(int) % modulus
    return  matrix_modulus_inv

def encrypt(message, K):
    encrypted = " "
    message_in_numbers = []
    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [message_in_numbers[i: i + int(K.shape[0])] for i in
               range(0, len(message_in_numbers), int(K.shape[0]))]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index["x"])[:,np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted



def decrypt(cipher, Kinv):
    decrypted = " "
    cipher_in_numbers = []
    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [cipher_in_numbers[i: i + int(Kinv.shape[0])] for i in
               range(0, len(cipher_in_numbers), int(Kinv.shape[0]))]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted

def main():
    message = "act"
    cipher = "poh"
    modulus = len(alphabet)
    key = np.array([[6, 24, 1],
                    [13, 16, 10],
                    [20, 17, 15]])


    Kinv = matrix_mod_inv(key, modulus)

    print(f"The decrypted message is: {decrypt(cipher, Kinv)}")
    print(f"The encrypted message is: {encrypt(message, key)}")

main()
print("Hello")



















