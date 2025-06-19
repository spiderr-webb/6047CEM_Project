from qiskit import QuantumCircuit, execute
from qiskit_aer import AerSimulator
from IPython.display import display
from matplotlib import pyplot
import math
from qrng import QRNG


class alice_bb84:

    # def __init__(self):

    '''
    def rand_bits(self, length):

        bitarray = []

        for i in range(0, length):
            bitarray.append(random.randint(0, 1))

        # bitstring = ''.join(str(bit) for bit in bitarray)

        return bitarray
    '''

    def alice_1(self, message):

        # calculate length needed for inital key
        length_in_bytes = int(math.ceil(len(message) * 2.25) + 2)

        # create quantum random number generation process
        qrng = QRNG()

        # generate random bitstream of specified length to use as initial key
        self.alice_key = qrng.generate(length_in_bytes)  # self.rand_bits(length)

        # generate random bitstream of specified length to decide where to apply hadamard gates
        self.alice_gates = qrng.generate(length_in_bytes)  # self.rand_bits(length)

        #print("Alice Key:        " + ''.join(str(bit) for bit in self.alice_key))
        #print("                  " + str(len(self.alice_key)))
        #print("Alice Gates: " + ''.join(str(bit) for bit in self.alice_gates))
        #print("                  " + str(len(self.alice_gates)))

        # initialise array to store quantum circuits
        circuits = []

        # for each byte in generated random bitstreams
        for r in range(0, length_in_bytes):

            # create quantum circuit with 8 qubits and append to circuits array
            circuits.append(QuantumCircuit(8))

            # for each qubit in circuit
            for q in range(0, 8):

                # if corresponding bit of initial key bitstream is 1
                if self.alice_key[(r*8 + q)] == 1:

                    # apply pauli-x gate to qubit
                    circuits[r].x(q)

                # if corresponding bit of gate-indicating bitstream is 1
                if self.alice_gates[(r*8 + q)] == 1:

                    # apply hadamard gate to qubit
                    circuits[r].h(q)

            # draw and display circuit diagram for quantum circuit
            # display(circuits[r].draw("mpl"))
            # pyplot.show()

        # return array of quantum circuits (aka send qubits to Bob)
        return circuits

    def alice_2(self, bob_gates):

        # initialise array to show positions of shared key bits
        comparison = []

        # initialise Alice's shared key string
        self.shared_key = ""

        # for each bit in Alice's gate-indicating bitstream
        for count in range(0, len(self.alice_gates)):

            # if bit of Bob's gate-indicating bitstream is same as Alice's gate-indicating bitstream
            if self.alice_gates[count] == bob_gates[count]:

                # add corresponding bit of initial key to Alice's shared key
                self.shared_key += str(self.alice_key[count])

                # add 1 to array showing positions of shared key bits
                comparison.append(1)

            # if bit of Bob's gate-indicating bitstream is different from Alice's gate-indicating bitstream
            else:

                # add 0 to array showing positions of shared key bits
                comparison.append(0)

        # return array showing positions of shared key bits
        return comparison

    def alice_3(self, bob_check, message):

        # initialise boolean value showing if key is usable
        valid = False

        # remove first 2 bytes from shared key to check that Alice and Bob's keys match
        alice_check = self.shared_key[:16]
        self.shared_key = self.shared_key[16:]

        # if Alice and Bob's check bytes match and remaining key is long enough for message
        if alice_check == bob_check and (len(self.shared_key) / 8) >= len(message):

            # set valid to true to show key is usable
            valid = True

        # return value showing if key is usable
        return self.shared_key, valid
