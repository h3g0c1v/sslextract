#!/usr/bin/env python3

# Libraries
from colorama import Fore, Style
import argparse, os, subprocess, re

# Colors
white = Fore.WHITE
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
red = Fore.RED
reset = Style.RESET_ALL

# Parameter management
parser = argparse.ArgumentParser(description="Filtering sensitive information from an SSL certificate")
parser.add_argument('-i','--ip', type=str, required=True, help='Destination IP address')
parser.add_argument('-p', '--port', type=int, required=True, help='Destination port')
args = parser.parse_args()

# Global variables
ip = args.ip
port = args.port

# Function to validate the IP address
def validateIP(ip):
    validIp = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip)
    
    if validIp:
        return 0
    else:
        print(f"\n{white}[{red}ERROR{reset}]: The IP address entered is NOT valid.")
        exit(1)

# Function to validate the port
def validatePort(port):
    # Check if the entered port is an integer
    if not isinstance(port, int):
        print(f"\n{white}[{red}ERROR{reset}]: The specified port must be an integer.")
        exit(1)
    
    # Check if the port is within the valid range
    if port < 1 or port > 65535:
        print(f"\n{white}[{red}ERROR{reset}]: The specified port is NOT valid. It must be between 1 and 65535.")
        exit(1)

# Check if the openssl command is installed
def opensslValidate():
    if subprocess.run("which openssl", shell=True, capture_output=True).returncode != 0:
        print(f"{white}[{red}ERROR{reset}]: OpenSSL is not installed or not found in the PATH.")
        exit(1)

# Function to extract information from the SSL certificate
def obtainCert(ip, port, certFile=".cert.ca.tmp"):
    command = f"openssl s_client -connect {ip}:{port} </dev/null | openssl x509 -text > {certFile}"

    try:  # Try to obtain the SSL certificate
        subprocess.run(command, shell=True, capture_output=True, text=True, check=True, timeout=10)
        
        with open(certFile, "r") as file:
            return file.read()

    except subprocess.TimeoutExpired:  # In case of a timeout
        print(f"\n{white}[{red}ERROR{reset}]: The command took too long to respond\n")

    except Exception as e:  # If something goes wrong, it will show the corresponding error
        print(f"\n{white}[{red}ERROR{reset}]: {e}")
    
    finally:  # Delete the generated file to obtain the certificate
        os.remove(certFile) if os.path.exists(certFile) else ""

# Extracting information from the SSL certificate
def extractInfo(certContent):
    domain = re.findall(r"\b\w+\.[A-Za-z-._]+\b", certContent)
    email = re.findall(r"\b[A-Za-z0-9._+-]+@\w+\.\w{2,}\b", certContent)
    ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", certContent)
    
    country = re.findall(r"\/C=([A-Z]{2})", certContent)
    province = re.findall(r"\/ST=([A-Za-z ]+)\/", certContent)
    location = re.findall(r"\/L=([A-Za-z ]+)\/", certContent)

    validity = re.findall(r"\bNot After : (.*)", certContent)

    return {"domain": domain, "email": email, "ip": ip, "country": country, "province": province, "location": location, "validity": validity}

# Showing the extracted sensitive information in a structured manner (reusing code)
def showExtractInfo(info, text):
    print(f"\n{white}[{green}i{reset}{white}] {text.capitalize()} found: {reset}")

    if not results[info]: 
        return print(f"\t{red}! NO{white} {text} found")

    last = ""
    for item in results[info]:
        if item != last:
            print(f"\t{yellow}+{reset} {blue}{item}{reset}")

        last = item

# Main function
if __name__ == '__main__':
    # Validating correct execution of the code (IP and port provided as parameters)
    validateIP(ip)
    validatePort(port)
    opensslValidate()

    certContent = obtainCert(ip, port)  # Getting the SSL certificate content
    results = extractInfo(certContent)  # Extracting sensitive information from the certificate

    # Storing the obtained information and its text in a dictionary for iteration (Purpose: code reuse)
    dictionary = {"domain": "domains / subdomains", "email": "email addresses", "ip": "IP addresses", "country": "countries", "province": "provinces", "location": "locations", "validity": "expiration date"}
    
    # Iterating over each extracted information and displaying it
    for info, text in dictionary.items():
        showExtractInfo(info, text)  # Showing the structured information
