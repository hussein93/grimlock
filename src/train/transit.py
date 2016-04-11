""" Script that handles interactions with Grimlock """
import sys
import os, pwd
import aiml
import pdb

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn('train/aiml/restaurants.aiml')

def process_command(message):
    response = ''
    if(message == 'food'):
        # pdb.set_trace()
        response = kernel.respond(message)
    else:
        response = message

    return response
