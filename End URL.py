import requests
import argparse
import pyfiglet

# Creating pyfiglet url banner text
def banner(text, font):
    pyfig = pyfiglet.figlet_format(text, font=font)
    return pyfig


# Finding end URL Link
# Exm url "https://shorturl.at/6XJMu"
def URL(link):
    req = requests.get(link)
    find = req.url
    return find

# Find Status code
def STATUS(st):
    req = requests.get(st)
    code = req.status_code
    return code


#Crating Help CLA
def help():
    print("usage of this script")
    print("usage > [script name] [optional argument] [target url]\n")
    print("-u ,", "--url         Target end url find")
    print("-s ,", "--status      Find url active or not")




# CML
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-u', '--url', action='store_true')
parser.add_argument('-s', '--status', action='store_true')
parser.add_argument('link', nargs="?", type=str)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('-f', '--file', action='store_true')

arg = parser.parse_args()

# pyfiglet text and font
if not arg.url and not arg.status:
    text = "URL"
    font = "doh"
    print(banner(text, font).rstrip())

    version = "Version >>> 1"
    print(version.center(90))


if arg.url:
    print(URL(arg.link))
# else:
#     print("Wrong url Short or Long form")

if arg.status:
    print(STATUS(arg.link))
# else:
#     print("Wrong status Short or Long form")

if arg.help:
    help()


# if not arg.url and not arg.status:
#     print("Type atlease one argument -u or -s")
#     print("Type -h or --help command")