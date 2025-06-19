from qiskit import QuantumCircuit, execute
from IPython.display import display
from matplotlib import pyplot
from qiskit_aer import AerSimulator


class QRNG:

    #def __init__(self):

        #out = self.generate(10)

        # print(out)
        # print(len(out))

        # print()

    def generate(self, length_in_bytes):

        # initialise string that will hold random byte result
        random_bitstring = ""

        # for specified number of bytes random bitstream needs to contain
        for y in range(0, length_in_bytes):

            # create quantum circuit with 8 qubits
            random_circuit = QuantumCircuit(8)

            # apply hadamard gate to each qubit
            for x in range(0, 8):
                random_circuit.h(x)

            # measure all qubits in circuit
            random_circuit.measure_all()

            # draw and display circuit diagram for quantum circuit
            # display(random_circuit.draw("mpl"))
            # pyplot.show()

            # create simulation
            sim = AerSimulator()

            # execute quantum circuit once and store result in dictionary
            results = execute(random_circuit, sim, shots=1).result()
            counts_dict = results.get_counts()

            # convert result to string and add to random bitstream
            random_bitstring += ("".join(list(counts_dict.keys())))

        # convert random bitstream string to array of bits
        random_bitarray = [int(bit) for bit in list(random_bitstring)]

        # return array of random bitstream
        return random_bitarray
