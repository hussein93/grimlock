""" Script for the AI Bot called Grimlock """
import sys
import os, pwd

from train.transit import process_command

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
            bot_response = process_command(message)
            print bot_response

if __name__ == '__main__':
    sys.exit(main())
