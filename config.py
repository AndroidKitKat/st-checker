import sys
import os
import json
import subprocess

data = {}
data['os_path'] = []
data['found'] = []


def detectConfig():
    if os.path.exists('config.json'):
        answer = input('A config.json already exists, running this program will overwrite it. Do you want to continue? (y/n):  ').lower()
        while not (answer.startswith('y') or answer.startswith('n')):
            answer = input('Try again (y/n): ').lower()
        if answer.startswith('y'):   # etc.
            generateConfig()
        elif answer.startswith('n'):
            print('Exiting...')
            sys.exit(0)
    else:
        generateConfig()

def generateConfig():
    with open('config.json', 'w+') as configFile:
        path = input('Input the path (from root) to the \'operatingsystem\' repo, ending with a \'/\', (if unsure, press return): ')
        print(path)
        if os.path.exists(path + 'input/operatingsystem.xml'):
            data['os_path'].append(path)
            data['found'].append('1')
            json.dump(data,configFile,indent = 2)
        else:
            findAndDL = input('Unable to find \'operatingsystem\' repo. A potentially outdated one will be downloaded and used.\nContinue? (y/n):')
            while not (findAndDL.startswith('y') or findAndDL.startswith('n')):
                findAndDL = input('Try again (y/n): ').lower()
            if findAndDL.startswith('y'):   # etc.
                subprocess.Popen(['curl','-soc','rules/OsRules.xsl','https://github.com/AndroidKitKat/st-checker/releases/download/whyDoINeedThis/OsRules.xsl'])
                data['os_path'].append('rules/OsRules')
                data['found'].append('0')
                json.dump(data,configFile,indent = 2)
            elif findAndDL.startswith('n'):
                print('Exiting...')
                sys.exit(0)

detectConfig()