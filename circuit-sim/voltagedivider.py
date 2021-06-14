import numpy as np
import matplotlib.pyplot as plt
import sys
import PySpice
import PySpice.Logging.Logging as Logging

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *


logger = Logging.setup_logging()

if sys.platform == "linux" or sys.platform == "linux2":
    PySpice.Spice.Simulation.CircuitSimulator.DEFAULT_SIMULATOR = 'ngspice-subprocess' #needed for this to run on linux
elif sys.platform == "win32":
    pass

#create the circuit instance itself

circuit = Circuit(':Voltage Divider')
# Adding compenent to the circuit
#Voltage source:
circuit.V('input', 'in', circuit.gnd, 10@u_V)
#add a resistor:
circuit.R(1, 'in', 'out', 9@u_kOhm)
#adds a resistor 2:
circuit.R(2, 'out', circuit.gnd, 1@u_kOhm)

#To simulate the circuit with actual parameters:
###
simulator = circuit.simulator(temperature=25, nominal_temprature=25)


#print the circuit:
print("The Circuit/Netlist:\n\n", circuit)

#Print the simulator instance:
###
print("Simulator:\n", simulator)


#Analysis code
######################3
analysis = simulator.operating_point()

print (analysis)
## to properly print out the analysis, we need to specify the data_type and node name.

print(analysis.nodes['in'])
print(str(analysis['in']))
print(float(analysis['in']))


#Out
print(analysis.nodes['out'])
print(str(analysis['out']))
print(float(analysis['out']))
exit()


