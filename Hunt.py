import urllib.request
import urllib.error
import argparse
import socket
import ipaddress

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory", help="bruteforce directory (inform the domain ex: google.com, facebook.com)")
parser.add_argument("-D", "--domain", help="bruteforce subdomains (inform the domain ex: google.com, facebook.com)")
parser.add_argument("-w", "--wordlist", help="indicate one wordlist archive", required=True)
parser.add_argument("-u", "--useragent", help="set user-agent archive")
parser.add_argument("-a", "--all", help="makes a bruteforce of directories and subdomains in a domain")
parser.add_argument("-o", "--output", help="creates a file with the output: pls set the nameof archive, ex: '-o nameofarchive.txt'")

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
def bruteDirectoryOutput(domain, wordlist, nameArq):
    arq = open(nameArq, "a")
    
    arq.write("The Directorys: \n")
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
    

    print(f"Trying Brute-force in Directorys on {domain} [{ip}]...")
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
        
        print(f"http://{domain}/{directory}", end="\r")

    print("                                           ")
    print("is this...")
    arq.write("\n")
    arq.close()

# NO output
def bruteDirectory(domain, wordlist):
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
    

    print(f"Trying Brute-force in Directorys on {domain} [{ip}]...")
    print("")        

    for directory in wordlist:
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{directory}"))

            if (req.status == 200):
                print(f"http://{domain}/{directory}: {req.status}")
                
        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domain}/{directory}: {code}")
        
        except urllib.error.URLError as error:
            print("URL invalid")
            print(error)
        
        print(f"http://{domain}/{directory}", end="\r")

    print("                                           ")
    print("is this...")


# Using user-agent
def bruteDirectoryUserOutput(domain, wordlist, useragent, nameArq):
    arq = open(nameArq, "a")
    
    arq.write("The Directorys: \n")
    arq.write("\n")

    useragent = {"user-agent": useragent}

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

    print(f"Trying Brute-force in Directorys on {domain} [{ip}]...")
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

    print(f"http://{domain}/{directory}", end="\r")

    print("                                           ")
    print("is this...")
    arq.write("\n")
    arq.close()


# User agent no output

def bruteDirectoryUser(domain, wordlist, useragent):
    useragent = {"user-agent": useragent}

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

    print(f"Trying Brute-force in Directorys on {domain} [{ip}]...")
    print("")

    for directory in wordlist: 
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{directory}", headers=useragent))

            if (req.status == 200 or req.code == 403):
                print(f"http://{domain}/{directory}: {req.status}")

        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domain}/{directory}: {code}")

        except urllib.error.URLError as error:
            print("URL invalid")
            print(error)

    print(f"http://{domain}/{directory}", end="\r")

    print("                                           ")
    print("is this...")

    

# ============================================================================


# Bruteforce Sub-domains
# ============================================================================
def bruteSubDomainOutput(domain, wordlist, nameArq):
    arq = open(nameArq, "a")
    
    arq.write("The Subdomains: \n")
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

    print(f"Trying Brute-force Subdomains {domain} [{ip}]...")
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

   
        print(f"http://{domains}.{domain}/", end="\r")

    print("                                           ")
    print("is this...")
    arq.write("\n")
    arq.close()


#NO output
def bruteSubDomain(domain, wordlist):
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

    print(f"Trying Brute-force Subdomains {domain} [{ip}]...")
    print("")

    for domains in wordlist:
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domains}.{domain}"))

            if (req.status == 200):
                print(f"http://{domains}.{domain}: {req.status}")
        
        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domains}.{domain}: {code}")

        except urllib.error.URLError as error:
            pass

   
        print(f"http://{domains}.{domain}/", end="\r")

    print("                                           ")
    print("is this...")




# Using user-agent
def bruteSubDomainUserOutput(domain, wordlist, useragent, nameArq):
    arq = open(nameArq, "a")

    arq.write("The Subdomains: \n")
    arq.write("\n")

    useragent = {"user-agent": useragent}


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

    print(f"Trying Brute-force Subdomains {domain} [{ip}]...")
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
        
        print(f"http://{domains}.{domain}/", end="\r")

    print("                                           ")
    print("is this...")
    arq.write("\n")
    arq.close()
    
#User agent no output
def bruteSubDomainUser(domain, wordlist, useragent):
    useragent = {"user-agent": useragent}

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

    print(f"Trying Brute-force Subdomains {domain} [{ip}]...")
    print("")

    for domains in wordlist:
        try:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domains}.{domain}", headers=useragent))

            if (req.status == 200):
                print(f"http://{domains}.{domain}: {req.status}")


        except urllib.error.HTTPError as error:
            code = error.code

            if (code != 404):
                print(f"http://{domains}.{domain}: {code}\n")
                        
        except urllib.error.URLError as error:
            pass
        
        print(f"http://{domains}.{domain}/", end="\r")

    print("                                           ")
    print("is this...")


# ============================================================================

try:
    wordlist = open(arguments.wordlist, "r").read().split("\n")

except FileNotFoundError:
    print("the wordlist arquive not found")
    exit()

if arguments.directory:
    typeBrute = arguments.directory

    if arguments.output:
        name = arguments.output

        if arguments.useragent:

            try:
                useragent = open(arguments.useragent, "r").read()
            
            except FileNotFoundError:
                print("the useragent arquive not found")
                exit()

            try:        
                menu()
                bruteDirectoryUserOutput(typeBrute, wordlist, useragent, name)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")

        else:
            try:
                menu()
                bruteDirectoryOutput(typeBrute, wordlist, name)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")
    else:
        if arguments.useragent:

            try:
                useragent = open(arguments.useragent, "r").read()
            
            except FileNotFoundError:
                print("the useragent arquive not found")
                exit()

            try:        
                menu()
                bruteDirectoryUser(typeBrute, wordlist, useragent)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")

        else:
            try:
                menu()
                bruteDirectory(typeBrute, wordlist)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")


elif arguments.domain:
    typeBrute = arguments.domain
    if arguments.output:
        name = arguments.output

        if arguments.useragent:

            try: 
                menu()
                useragent = open(arguments.useragent, "r").read()
                bruteSubDomainUserOutput(typeBrute, wordlist, useragent, name)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")

        else:
            try:
                menu()
                bruteSubDomainOutput(typeBrute, wordlist, name)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")
    
    else:
        if arguments.useragent:

            try: 
                menu()
                useragent = open(arguments.useragent, "r").read()
                bruteSubDomainUser(typeBrute, wordlist, useragent)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")

        else:
            try:
                menu()
                bruteSubDomain(typeBrute, wordlist)
                exit()

            except KeyboardInterrupt:
                print("Bye Bye")


elif arguments.all:
    typeBrute = arguments.all 

    if arguments.output:
        name = arguments.output

        if arguments.useragent:
            try:
                menu()
                useragent = open(arguments.useragent, "r").read()
                bruteDirectoryUserOutput(typeBrute, wordlist, useragent, name)
                bruteSubDomainUserOutput(typeBrute, wordlist, useragent, name)
            except KeyboardInterrupt:
                print("Bye Bye")

        else:
            try:
                menu()
                bruteDirectoryOutput(typeBrute, wordlist, name)
                bruteSubDomainOutput(typeBrute, wordlist, name)
            except KeyboardInterrupt:
                print("Bye Bye")
    
    else:
        if arguments.useragent:
            try:
                menu()
                useragent = open(arguments.useragent, "r").read()
                bruteDirectoryUser(typeBrute, wordlist, useragent)
                bruteSubDomainUser(typeBrute, wordlist, useragent)
            except KeyboardInterrupt:
                print("Bye Bye")

        else:
            try:
                menu()
                bruteDirectory(typeBrute, wordlist)
                bruteSubDomain(typeBrute, wordlist)
            except KeyboardInterrupt:
                print("Bye Bye")