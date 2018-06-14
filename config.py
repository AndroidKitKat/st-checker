import sys
import os

# import yaml

# data = dict(
#     A = 'a',
#     B = dict(
#         C = 'c',
#         D = 'd',
#         E = 'e',
#     )
# )

# with open('data.yml', 'w') as outfile:
#     yaml.dump(data, outfile, default_flow_style=False)


def generateConfig():
    with open('config.ini', 'a+') as configFile:
        path = input('Input the path to the operatingsystems repo, if you don\'t know where this is, just hit "return" and I will try to find it.\n')
        configFile.write(path)

generateConfig()