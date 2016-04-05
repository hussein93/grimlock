""" Script for the AI Bot called Grimlock """
import sys
import os, pwd
import pdb
import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn('std-startup.xml')
kernel.respond('load aiml b')

def main():
    """Main entry point for the script."""
    user = pwd.getpwuid(os.getuid()).pw_name

    # Interaction with Grimlock
    while True:
        message = raw_input(user + '> ')
        if (message == 'quit' or message == 'Quit'):
            exit()
        elif message == 'save':
            print('Grimlock will remember this conversation.')
            #kernel.saveBrain('bot_brain.brn')
        else:
            print('Still in production')
            #bot_response = kernel.respond(message)

if __name__ == '__main__':
    sys.exit(main())
