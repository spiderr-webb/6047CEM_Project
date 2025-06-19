# 6047CEM_Project

## Introduction

Welcome to the repository for my dissertation project for the module <b><i>6047CEM Cyber Security Project</i></b> - completed January-April 2024

## What It Does

This program was created to simulate a payment transaction involving three parties - the buyer, the merchant, and the bank - in order to demonstrate the encryption protocol designed as part of this coursework, and to show how it would ensure that the transaction remains secure.

The project directory contains the following files:

`qrng.py` - Contains functions that can be used by both parties in a communication to carry out a Diffie-Hellman key exchange

`bb84_alice.py` - Contains functions to encrypt and decrypt using AES

`bb84_bob.py` - Contains a function to calculate the SHA-256 hash of an input

`auth.py` - Contains functions to generate and check the validity of digital signatures using RSA

`connection.py` - Shows the flow of information between the three parties involved, including where the above methods would be implemented to ensure security

## How To Use

All files in the directory are required for the program to run.

### Module Requirements

The following modules will need to be installed for all parts of the 
program to run correctly:


### Running the program

Once these have been downloaded, the program can be run from the CLI by navigating to the project directory and running the command:

`python3 exchange.py`

## Documentation

The developer documentation for this program is provided in the form of 
docstrings and comments in the source-code.
