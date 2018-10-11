"""
Author: ELF
Course: Python
version: Python 2.7
FileName: chatServer.py
Lab5A
Instructions:
    Write a TCP Server that will generate a random number from 0 to 100
    Then write a TCP Client that will receive an input from the user
    (number 0 to 100) and send the guess to the server. The server will
    then send back a message prompting the user to guess higher or lower. 
    If the user guesses the correct number, have the server send back a 
    success message and when the client receives the success message it 
    will break the connection (close the socket).
""" 
