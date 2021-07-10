import urllib.request
import urllib.error
import argparse
import socket
import ipaddress

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory", help="Use -d or --directory for bruteforce directory (inform the domain")
parser.add_argument("-D", "--domain", help="Use -D or --domain for bruteforce subdomains (inform the domain)")
parser.add_argument("-w", "--wordlist", help="Use -w or --wordlist to indicate one wordlist archive", required=True)
parser.add_argument("-u", "--useragent", help="Use -u or --useragent to set user-agent archive")


arguments = parser.parse_args()


# The Menu
def menu():
    print(" /$$   /$$                       /$$      ")  
    print("| $$  | $$                      | $$      ")
    print("| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    ")
    print("| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/    ")
    print("| $$__  $$| $$  | $$| $$  \ $$  | $$      ") 
    print("| $$  | $$| $$  | $$| $$  | $$  | $$ /$$  ")
    print("| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/  ")
    print("|__/  |__/ \______/ |__/  |__/   \___/    ")
    print("|")
    print("|- By sh4d0wgh0s7")
    print("")


def clear():
    import os 
    if (os.name == "nt"):
        os.system("cls")
    
    else:
        os.system("clear")


# CheckIp (Is very failed)
def checkIp(domain):
    pointCounter = 0

    for digito in domain:     
        if (digito.isdigit() == True or digito == "."):
            if (digito == "."):
                pointCounter += 1 

        elif(digito.isdigit() == False):
            return False
    
    if pointCounter == 3:
        return True



# Bruteforce in Directory 
# ============================================================================
def bruteDirectory(domain, wordlist):
    arq = open("BruteDirectory.txt", "a")
    
    arq.write(" /$$   /$$                       /$$      \n")  
    arq.write("| $$  | $$                      | $$      \n")
    arq.write("| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    \n")
    arq.write("| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/    \n")
    arq.write("| $$__  $$| $$  | $$| $$  \ $$ :| $$      \n") 
    arq.write("| $$  | $$| $$  | $$| $$  | $$  | $$ /$$  \n")
    arq.write("| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/  \n")
    arq.write("|__/  |__/ \______/ |__/  |__/   \___/    \n")
    arq.write("|\n")
    arq.write("|- By sh4d0wgh0s7\n")
    arq.write("\n")

    isIp = checkIp(domain)

    if (isIp == False):
        try:
            ip = str(socket.gethostbyname(domain))

        except socket.gaierror:
            ip = str("could not solve the domain for ip")

    else:
        try:
            ip = str(ipaddress.ip_address(domain))

        except ValueError:
            print("this ip is not valid")
            exit()
    
    clear()
    menu()
    print(f"Trying on {domain} [{ip}]...")
    print("")        

    for directory in wordlist:
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{directory}"))

            if (req.status == 200):
                print(f"http://{domain}/{directory}: {req.status}")
                arq.write(f"http://{domain}/{directory}: {req.status}\n")

        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domain}/{directory}: {code}")
                arq.write(f"http://{domain}/{directory}: {code}\n")  
        
        except urllib.error.URLError as error:
            print("URL invalid")
            print(error)
        

    print("")
    print("is this...")
    arq.close()


# Using user-agent
def bruteDirectoryUser(domain, wordlist, useragent):
    arq = open("BruteDirectoryUser.txt", "a")
    useragent = {"user-agent": useragent}
    
    arq.write(" /$$   /$$                       /$$      \n")  
    arq.write("| $$  | $$                      | $$      \n")
    arq.write("| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    \n")
    arq.write("| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/    \n")
    arq.write("| $$__  $$| $$  | $$| $$  \ $$  | $$      \n") 
    arq.write("| $$  | $$| $$  | $$| $$  | $$  | $$ /$$  \n")
    arq.write("| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/  \n")
    arq.write("|__/  |__/ \______/ |__/  |__/   \___/    \n")
    arq.write("|\n")
    arq.write("|- By sh4d0wgh0s7\n")
    arq.write("\n")

    isIp = checkIp(domain)

    if (isIp == False):
        try:
            ip = str(socket.gethostbyname(domain))

        except socket.gaierror:
            ip = str("could not solve the domain for ip")

    else:
        try:
            ip = str(ipaddress.ip_address(domain))

        except ValueError:
            print("this ip is not valid")
            exit()

    clear()
    menu()
    print(f"Trying on {domain} [{ip}]...")
    print("")

    for directory in wordlist: 
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{directory}", headers=useragent))

            if (req.status == 200 or req.code == 403):
                print(f"http://{domain}/{directory}: {req.status}")
                arq.write(f"http://{domain}/{directory}: {req.status}\n")

        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domain}/{directory}: {code}")
                arq.write(f"http://{domain}/{directory}: {code}\n")

        except urllib.error.URLError as error:
            print("URL invalid")
            print(error)

    print("")
    print("is this...")
    arq.close()
    

# ============================================================================


# Bruteforce Sub-domains
# ============================================================================
def bruteSubDomain(domain, wordlist):
    arq = open("BruteSubDomain.txt", "a")
    
    arq.write(" /$$   /$$                       /$$      \n")  
    arq.write("| $$  | $$                      | $$      \n")
    arq.write("| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    \n")
    arq.write("| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/    \n")
    arq.write("| $$__  $$| $$  | $$| $$  \ $$  | $$      \n") 
    arq.write("| $$  | $$| $$  | $$| $$  | $$  | $$ /$$  \n")
    arq.write("| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/  \n")
    arq.write("|__/  |__/ \______/ |__/  |__/   \___/    \n")
    arq.write("|\n")
    arq.write("|- By sh4d0wgh0s7\n")
    arq.write("\n") 

    isIp = checkIp(domain)

    if (isIp == False):
        try:
            ip = str(socket.gethostbyname(domain))

        except socket.gaierror:
            ip = str("could not solve the domain for ip")

    else:
        try:
            ip = str(ipaddress.ip_address(domain))

        except ValueError:
            print("this ip is not valid")
            exit()

    clear()
    menu()
    print(f"Trying on {domain} [{ip}]...")
    print("")

    for domains in wordlist:
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domains}.{domain}"))

            if (req.status == 200):
                print(f"http://{domains}.{domain}: {req.status}")
                arq.write(f"http://{domains}.{domain}: {req.status}\n")
        
        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domains}.{domain}: {code}")
                arq.write(f"http://{domains}.{domain}: {code}\n")

        except urllib.error.URLError as error:
            pass

   
    print("")
    print("is this...")
    arq.close()
    

# Using user-agent
def bruteSubDomainUser(domain, wordlist, useragent):
    arq = open("BruteSubDomainUser.txt", "a")
    useragent = {"user-agent": useragent}
    
    arq.write(" /$$   /$$                       /$$      \n")  
    arq.write("| $$  | $$                      | $$      \n")
    arq.write("| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    \n")
    arq.write("| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/    \n")
    arq.write("| $$__  $$| $$  | $$| $$  \ $$  | $$      \n") 
    arq.write("| $$  | $$| $$  | $$| $$  | $$  | $$ /$$  \n")
    arq.write("| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/  \n")
    arq.write("|__/  |__/ \______/ |__/  |__/   \___/    \n")
    arq.write("|\n")
    arq.write("|- By sh4d0wgh0s7\n")
    arq.write("\n")

    isIp = checkIp(domain)

    if (isIp == False):
        try:
            ip = str(socket.gethostbyname(domain))

        except socket.gaierror:
            ip = str("could not solve the domain for ip")

    else:
        try:
            ip = str(ipaddress.ip_address(domain))

        except ValueError:
            print("this ip is not valid")
            exit()

    clear()
    menu()
    print(f"Trying on {domain} [{ip}]...")
    print("")

    for domains in wordlist:
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domains}.{domain}", headers=useragent))

            if (req.status == 200):
                print(f"http://{domains}.{domain}: {req.status}")
                arq.write(f"http://{domains}.{domain}: {req.status}\n")


        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domains}.{domain}: {code}\n")
                arq.write(f"http://{domains}.{domain}: {code}\n")
                        
        except urllib.error.URLError as error:
            pass
        
        
    print("")
    print("is this...")
    arq.close()
    


# ============================================================================

#if arguments.help:
#    help()
#    exit()


try:
    wordlist = open(arguments.wordlist, "r").read().split("\n")

except FileNotFoundError:
    print("the wordlist arquive not found")
    exit()

if arguments.directory:
    typeBrute = arguments.directory

    if arguments.useragent:

        try:
            useragent = open(arguments.useragent, "r").read()
        
        except FileNotFoundError:
            print("the useragent arquive not found")
            exit()

        try:        
            bruteDirectoryUser(typeBrute, wordlist, useragent)
            exit()

        except KeyboardInterrupt:
            print("Bye Bye")

    else:
        try:
            bruteDirectory(typeBrute, wordlist)
            exit()

        except KeyboardInterrupt:
            print("Bye Bye")


elif arguments.domain:
    typeBrute = arguments.domain

    if arguments.useragent:

        try: 
            useragent = open(arguments.useragent, "r").read()
            bruteSubDomainUser(typeBrute, wordlist, useragent)
            exit()

        except KeyboardInterrupt:
            print("Bye Bye")

    else:
        try:
            bruteSubDomain(typeBrute, wordlist)
            exit()

        except KeyboardInterrupt:
            print("Bye Bye")


elif arguments.directory and arguments.domain:
    print("error cannot be used two functions at once")