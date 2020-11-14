import requests
import argparse
import json
from colorama import Fore, Back, Style 

def main_logo():

    print(" _____           _                 _____ _   _ ") 
    print("/  ___|         | |               /  __ \ | | |")
    print("\ `--. _   _ ___| |_ ___ _ __ ___ | /  \/ |_| |")
    print(" `--. \ | | / __| __/ _ \ '_ ` _ \| |   | __| |")
    print("/\__/ / |_| \__ \ ||  __/ | | | | | \__/\ |_| |")
    print("\____/ \__, |___/\__\___|_| |_| |_|\____/\__|_|")
    print("        __/ |                              ") 
    print("       |___/                                   ") 

if __name__=="__main__":
    main_logo()
    print(Fore.RED + '-----------------++++++++++++++-----------------')    
    print(Fore.RED + '-----------------Victim Details-----------------') 
    print(Fore.RED + '-----------------++++++++++++++-----------------')
    print(Style.RESET_ALL) 
    parser=argparse.ArgumentParser()
    
    parser.add_argument("-i","--ipaddress",help="-h")
    
    args=parser.parse_args()
    
    ip=args.ipaddress
    
    url="http://ip-api.com/json/"+ip
    
    response=requests.get(url)
    
    data=json.loads(response.content)
    
        
    print("\t[+] IP\t\t\t",data["query"])
    print("\t[+] CITY\t\t",data["city"])
    print("\t[+] ISP\t\t\t",data["isp"])
    print("\t[+] LOC\t\t\t",data["country"])
    print("\t[+] REG\t\t\t",data["regionName"])
    print("\t[+] TIME\t\t",data["timezone"])
    print("\t[+] ZIP\t\t\t",data["zip"])
    print("\t[+] LAT\t\t\t",data["lat"])
    print("\t[+] LON\t\t\t",data["lon"])
 
