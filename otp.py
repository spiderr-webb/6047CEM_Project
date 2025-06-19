class one_time_pad:

    def string_to_binary(self, string):

        # initialise string to store binary of message
        binary = ""

        # for each character in string
        for char in string:

            # convert character to 8 bit ASCII value and add to binary string
            binary += format(ord(char), '08b')

        # convert string to array of bits
        bitarray = list(binary)

        # return array of message binary bits
        return bitarray

    def encrypt(self, message, key):

        # convert message string to binary array
        plaintext = self.string_to_binary(message)

        # initialise array for ciphertext binary
        cipher_bits = []

        # for each byte in plaintext binary
        for x in range(0, len(plaintext) // 8):

            # join bits of plaintext binary array into byte
            plain_byte = int(''.join(plaintext[x*8:x*8+8]), 2)

            # join bits of key binary array into byte
            key_byte = int(''.join(key[x*8:x*8+8]), 2)

            # calculate value of ciphertext byte
            cipher_byte = ((plain_byte + key_byte) % 96) + 32

            # convert ciphertext byte into array of bits and add to ciphertext binary array
            cipher_bits += list(str('{0:08b}'.format(cipher_byte)))

        # convert ciphertext binary array to string
        ciphertext = self.binary_to_string(cipher_bits)

        # return ciphertext string
        return ciphertext

    def binary_to_string(self, binary):

        # initialise string to store message
        string = ""

        # for each byte in binary array
        for x in range(0, len(binary) // 8):

            # join bits of binary array into byte, convert byte to ASCII character and add to message string
            string += chr(int(''.join(binary[x*8:x*8+8]), 2))

        # return message string
        return string

    def decrypt(self, message, key):

        # convert ciphertext string to binary array
        ciphertext = self.string_to_binary(message)

        # initialise array for plaintext binary
        plain_bits = []

        # for each byte in ciphertext binary
        for x in range(0, len(ciphertext) // 8):

            # join bits of ciphertext binary array into byte
            cipher_byte = int(''.join(ciphertext[x*8:x*8+8]), 2)

            # join bits of key binary array into byte
            key_byte = int(''.join(key[x*8:x*8+8]), 2)

            # calculate value of plaintext byte
            plain_byte = (cipher_byte - 32) - key_byte

            while plain_byte < 32:
                plain_byte += 96

            # convert plaintext byte into array of bits and add to plaintext binary array
            plain_bits += list(str('{0:08b}'.format(plain_byte)))

        # convert plaintext binary array to string
        plaintext = self.binary_to_string(plain_bits)

        # return plaintext string
        return plaintext
