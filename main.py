import socket
from platform import node, system, release; Node, System, Release = node(), system(), release() 
from time import sleep

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.01)

r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'

printLow(f"""

{r}██████╗ ██████╗  ██████╗ ████████╗   ███████╗ ██████╗ █████╗ ███╗   ██╗███████╗██████╗ 
{r}██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝   ██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
{w}██████╔╝██████╔╝██║   ██║   ██║█████╗███████╗██║     ███████║██╔██╗ ██║█████╗  ██████╔╝
{w}██╔═══╝ ██╔══██╗██║   ██║   ██║╚════╝╚════██║██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
{g}██║     ██║  ██║╚██████╔╝   ██║      ███████║╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║
{g}╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

    {y}[*] Info:
    {g}[+] {y}Telegram-PV: {w}@Error_fiat  
    {g}[+] {y}Github: {w}https://github.com/errorfiathck 
    {g}[+] {y}Instagram: {w}https://instagram.com/error._.fiat  
    {g}[+] {y}Youtube: {w}https://youtube.com/error_fiat  
    
    {y}system:\n    {g}[+] {y}Platform: {w}{System}          
    {g}[+] {y}Node: {w}{Node}\n    {g}[+] {y}Release: {w}{Release}   \n\n                                                                   
""")

ip = input(f"{g}Enter the target IP ==>")
prot_list = [20, 80, 8080, 139, 445, 23, 21, 22]

for port in prot_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        print('_' * 60)
        print('Port: ', port, 'Open')
        print('_' * 60)

    else:
        print('Port: ', port, 'Closed')