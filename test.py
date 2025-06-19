from qiskit import QuantumCircuit, execute
from IPython.display import display
from matplotlib import pyplot
from qiskit_aer import AerSimulator

# initialise string to hold random bitstream
random = ""

# run loop 40,000 times
for y in range(0, 40000):

    # print number in loop to show how far through running the program is
    print(y)

    # create quantum circuit with 25 qubits
    circuit = QuantumCircuit(25)

    # apply hadamard gate to each qubit
    for x in range(0, 25):
        circuit.h(x)

    # measure all qubits in circuit
    circuit.measure_all()

    # draw and display circuit diagram for quantum circuit
    # display(circuit.draw("mpl"))
    # pyplot.show()

    # create simulation
    sim = AerSimulator()

    # execute quantum circuit once and store result in dictionary
    results = execute(circuit, sim, shots=1).result()
    counts_dict = results.get_counts()

    # convert result to string and add to random bitstream
    random += ("".join(list(counts_dict.keys())))

# write random bitstream to file
f = open("./file.txt", "w")
f.write(random)
f.close()

# print random bitstream
print(random)
