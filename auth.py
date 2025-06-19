from qiskit import QuantumCircuit, execute
from IPython.display import display
from matplotlib import pyplot
from qiskit_aer import AerSimulator
from qrng import QRNG


class authentication:

    def create_private(self, filepath):

        # set length of private key to generate to 10 bytes
        length = 10

        # create quantum random number generation process
        qrng = QRNG()

        # generate random bitstream of specified length to use as private key
        private_bitstream = "".join(map(str, qrng.generate(length)))

        # write private key to file at specified filepath
        file = open(filepath, "w")
        file.write(str("".join(str(private_bitstream))) + "\n")
        file.close()

    def create_public(self, private_filepath):

        # read private key from specified file
        file = open(private_filepath, "r")
        private_bitstream = list(map(int, file.readline().strip()))
        file.close()

        # initialise public key array
        public_key = []

        # for each bit in private key bitstream
        for i in range(0, len(private_bitstream)):

            # create quantum circuit with 1 qubit and append to public key array
            public_key.append(QuantumCircuit(1))

            # if corresponding bit of private key bitstream is 1
            if private_bitstream[i] == 1:

                # apply pauli-x gate to qubit
                public_key[i].x(0)

            # apply hadamard gate to qubit
            public_key[i].h(0)

        # return public key array
        return public_key

    def swap_test(self, test_key, trusted_key):

        # key is considered valid until proved invalid
        valid = True

        # for each qubit in public key to validate
        for y in range(0, len(test_key)):

            # create quantum circuit with 3 qubits and 1 classical bit
            swap_circuit = QuantumCircuit(3, 1)

            # add qubit from public key to validate into swap test circuit
            swap_circuit.compose(test_key[y], qubits=[1], inplace=True)

            # add qubit from trusted public key into swap test circuit
            swap_circuit.compose(trusted_key[y], qubits=[2], inplace=True)

            # apply hadamard gate to first qubit
            swap_circuit.h(0)

            # perform swap test on circuit
            swap_circuit.cswap(0, 1, 2)

            # apply hadamard gate to first qubit
            swap_circuit.h(0)

            # measure first qubit
            swap_circuit.measure(0, 0)

            # draw and display circuit diagram for quantum circuit
            # display(swap_circuit.draw("mpl"))
            # pyplot.show()

            # create simulation
            sim = AerSimulator()

            # execute quantum circuit once and store result in dictionary
            results = execute(swap_circuit, sim, shots=1).result()
            counts_dict = results.get_counts()

            # if result of swap test was 1 set valid to false
            if int("".join(list(counts_dict.keys()))) == 1:
                valid = False

        # return whether all swap tests were passed
        return valid
