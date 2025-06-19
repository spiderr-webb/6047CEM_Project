# 6047CEM_Project

## Introduction

Welcome to the repository for my dissertation project for the module <b><i>6047CEM Cyber Security Project</i></b> - completed January-April 2024

## What It Does

...

## How To Use

To run this program, the following files need to be downloaded:

`qrng.py` - Contains functions for quantum random number generation

`bb84_alice.py` - Contains functions for Alice’s side of the BB84 key exchange

`bb84_bob.py` - Contains functions for Bob’s side of the BB84 key exchange

`otp.py` - Contains functions for the one-time pad encryption and decryption

`auth.py` - Contains functions for the authentication system

`exchange.py` - Contains code for running all of the previous functions together, showing the flow of information throughout the system

Additionally, this repository contains the following files which are not required for the program to run:

`test.py` - Contains code for the alternate version of the quantum random number generator used to generate a longer bitstream, for use in randomness testing

### Module Requirements

The following modules will need to be installed for all parts of the 
program to run correctly:


### Running the program

The program can be run from the CLI by navigating to the project directory and running the command:

`python3 exchange.py`

## Documentation

The developer documentation for this program is provided in the form of 
docstrings and comments in the source-code.
