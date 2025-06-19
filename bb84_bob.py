from qiskit import execute
from qiskit_aer import AerSimulator
from IPython.display import display
from matplotlib import pyplot
from qrng import QRNG


class bob_bb84:

    def bob_1(self, circuits):

        # get number of bytes sent by Alice
        length_in_bytes = len(circuits)

        # create quantum random number generation process
        qrng = QRNG()

        # generate random bitstream of specified length to decide where to apply hadamard gates
        bob_gates = qrng.generate(length_in_bytes)  # self.rand_bits(length)

        # for each byte sent from Alice
        for r in range(0, length_in_bytes):

            # for each qubit
            for q in range(0, 8):

                # if corresponding bit of gate-indicating bitstream is 1
                if bob_gates[(r*8 + q)] == 1:

                    # apply hadamard gate to qubit
                    circuits[r].h(q)

            # measure all qubits in circuit
            circuits[r].measure_all()

        # get value of Bob's key by running simulations of all quantum circuits
        self.bob_key = self.run_sim(circuits)

        #print("Bob Gates:   " + ''.join(str(bit) for bit in bob_gates))
        #print("                  " + str(len(bob_gates)))
        #print("Bob Key:          " + ''.join(str(bit) for bit in self.bob_key))
        #print("                  " + str(len(self.bob_key)))

        # return bitstream showing where hadamard gates were applied by Bob
        return bob_gates

    def bob_2(self, comparison):

        # initialise Bob's shared key string
        shared_key = ""

        # for each bit in array showing positions of shared key bits
        for count in range(0, len(comparison)):

            # if comparison bitstream indicates corresponding bits of Alice and Bob's keys are shared
            if comparison[count] == 1:

                # add corresponding bit of Bob's key to shared key
                shared_key += str(self.bob_key[count])

        # remove first 2 bytes from shared key to check that Alice and Bob's keys match
        check = shared_key[:16]
        shared_key = shared_key[16:]

        # return Bob's check bytes, and Bob's shared key to use for decryption
        return check, shared_key

    def run_sim(self, circuits):

        # initialise key string
        key_string = ""

        # for quantum circuit in array
        for c in circuits:

            # draw and display circuit diagram for quantum circuit
            # display(c.draw("mpl"))
            # pyplot.show()

            # create simulation
            sim = AerSimulator()

            # execute quantum circuit once and store result in dictionary
            results = execute(c, sim, shots=1).result()
            counts_dict = results.get_counts()

            # convert result byte to array of bits
            counts_list = list(counts_dict.keys())

            # reverse bits in result byte
            reversed = [i[::-1] for i in counts_list]

            # convert result to string and add to key
            key_string += ("".join(reversed))

        # convert key string to array of bits
        key_array = [int(bit) for bit in list(key_string)]

        # return array of key bits
        return key_array
