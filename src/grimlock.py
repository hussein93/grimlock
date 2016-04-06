""" Script for the AI Bot called Grimlock """
import sys
import os, pwd
import pdb
import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn('aiml/restaurants.aiml')

def main():
    """Main entry point for the script."""
    user = pwd.getpwuid(os.getuid()).pw_name
    bot_name = 'Grimlock'

    # Interaction with Grimlock
    while True:
        message = raw_input(user + '> ')
        if (message == 'quit' or message == 'Quit'):
            exit()
        elif message == 'save':
            print('Grimlock will remember this conversation.')
            #kernel.saveBrain('bot_brain.brn')
        else:
            #print(bot_name + '> I\'m still in production!')
            bot_response = kernel.respond(message)
            print bot_response

if __name__ == '__main__':
    sys.exit(main())
