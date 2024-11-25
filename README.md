# SSL Extract

**sslextract** is a Python tool that extracts key information from SSL certificates, such as domains, emails, IP addresses, and expiration dates, using `openssl`.

## Features

- Extract domains and subdomains from the SSL certificate
- Extract emails found in the certificate
- Extract IP addresses linked to the certificate
- Extract the certificate's expiration date
- Extract countries, provinces, and locations found in the certificate
- Colorized output for improved readability

## Requirements

- Python 3.x
- OpenSSL installed and accessible in the system's PATH

## Installation
Clone the repository:

```bash
git clone https://github.com/h3g0c1v/sslextract
cd sslextract
```

## Usage

Run the script by providing the target IP and port:

```bash
python sslextract.py -i <IP_ADDRESS> -p <PORT>
```

### Example:

```bash
python sslextract.py -i 10.10.11.102 -p 443
```

This will extract information from the SSL certificate of the given server.

## Options
- `-i`, `--ip`: Target IP address (required)
- `-p`, `--port`: Target port (required)

## Example Output

```bash
[i] Domains / subdomains found: 
	+ api.example.com
	+ example.com

[i] Email addresses found: 
	+ admin@example.com
	+ support@example.com

[i] Ip addresses found: 
	! NO IP addresses found

[i] Countries found: 
	+ US

[i] Provinces found: 
	+ California

[i] Locations found: 
	+ San Francisco

[i] Expiration date found: 
	+ May 24 19:54:56 2031 GMTT
```

I hope it helps you <3
