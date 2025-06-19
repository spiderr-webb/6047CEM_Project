from bb84_alice import alice_bb84
from bb84_bob import bob_bb84
from otp import one_time_pad
from auth import authentication


def alice_authenticate():

    # create Alice's authentication process
    alice = authentication()

    # create private key and store in Alice's private key file
    alice.create_private("keys/alice_private_key.txt")

    # create public key using private key in Alice's private key file
    alice_key = alice.create_public("keys/alice_private_key.txt")

    # return Alice's public key
    return alice_key


def eve_authenticate():

    # create Eve's authentication process
    eve = authentication()

    # create private key and store in Eve's private key file
    eve.create_private("keys/eve_private_key.txt")

    # create public key using private key in Eve's private key file
    eve_key = eve.create_public("keys/eve_private_key.txt")

    # return Eve's public key
    return eve_key


def alice_test(public_key):

    # create Bob's authentication process
    bob = authentication()

    # create trusted party's authentication process
    trusted = authentication()

    # trusted party - create public key using private key in Alice's private key file
    trusted_alice_key = trusted.create_public("keys/alice_private_key.txt")

    # Bob - perform swap test on input public key and trusted party generated public key
    is_alice = bob.swap_test(public_key, trusted_alice_key)

    # if swap test shows public keys are the same
    if is_alice:
        print("\nWelcome Alice! :)")

    # if swap test shows public keys are different
    else:
        print("\nNice try, Eve ;)")

    # return result of swap test
    return is_alice


def encrypt(plaintext, key):

    # create Alice's encryption process
    alice_otp = one_time_pad()

    # encrypt Alice's message using one-time pad
    ciphertext = alice_otp.encrypt(plaintext, key)

    # return encrypted message
    return ciphertext


def decrypt(ciphertext, key):

    # create Bob's decryption process
    bob_otp = one_time_pad()

    # decrypt Alice's message using one-time pad
    plaintext = bob_otp.decrypt(ciphertext, key)

    # return decrypted message
    return plaintext


if __name__ == '__main__':

    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    print("   AUTHENTICATION")
    print("~~~~~~~~~~~~~~~~~~~~~~\n")

    # initialise input string
    id = ""

    # while value of input string not valid
    while id != "ALICE" and id != "EVE":

        # get user input and convert to uppercase
        print("Would you like to try to connect as Alice or Eve?")
        id = input().upper()

        # if connecting as Alice
        if id == "ALICE":

            # generate Alice's public key
            public_key = alice_authenticate()

        # if connecting as Eve
        elif id == "EVE":

            # generate Eve's public key
            public_key = eve_authenticate()

        else:

            # print error message
            print("Try again - ", end="")

    # get results of Bob's swap test using specified public key
    is_alice = alice_test(public_key)

    # if public key identified as Alice's by swap test
    if is_alice:

        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print("     KEY EXCHANGE")
        print("~~~~~~~~~~~~~~~~~~~~~~\n")

        # get user input for message to send
        print("Enter the message you would like to send:")
        m = input()

        print()

        # set valid to false to ensure while loop runs at least once
        valid = False

        # while key generated not valid
        while not valid:

            # create Alice's BB84 process
            alice = alice_bb84()

            # create Bob's BB84 process
            bob = bob_bb84()

            # Alice - create qubits, apply gates and send to Bob
            circuits = alice.alice_1(m)

            # Bob - receive qubits, apply gates and send gates applied to Alice
            bob_gates = bob.bob_1(circuits)

            # Alice - receive gates applied by Bob, figure out which key bits are shared, send information to Bob
            comparison = alice.alice_2(bob_gates)

            # Bob - receive information about shared key bits, send part of shared key to Alice for error checking
            bob_check, bob_key = bob.bob_2(comparison)

            # Alice - receive part of Bob's shared key, compare to own shared key to confirm exchange was successful
            # also check shared key is long enough for message to be sent
            alice_key, valid = alice.alice_3(bob_check, m)

        # print shared keys held by Alice and Bob
        print("Alice key:  " + alice_key)
        print("Bob key:    " + bob_key)

        print("\n~~~~~~~~~~~~~~~~~~~~~~")
        print("      ENCRYPTION")
        print("~~~~~~~~~~~~~~~~~~~~~~\n")

        # encrypt message using Alice's shared key
        c = encrypt(m, alice_key)

        # print encrypted message
        print("Ciphertext encrypted by Alice:  " + c)
        print()

        # decrypt message using Bob's shared key
        p = decrypt(c, bob_key)

        # print decrypted message
        print("Plaintext decrypted by Bob:     " + p)

    print()
