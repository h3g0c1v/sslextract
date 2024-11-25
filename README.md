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
[i] Dominios / subdominios encontrados: 
	+ api.example.com
	+ example.com

[i] Correos electrónicos encontrados: 
	+ admin@example.com
	+ support@example.com

[i] Direcciones ip encontrados: 
	! NO se han encontrado direcciones IP

[i] Paises encontrados: 
	+ US

[i] Provincias encontrados: 
	+ California

[i] Localidades encontrados: 
	+ San Francisco

[i] Fecha de expiración encontrados: 
	+ May 24 19:54:56 2031 GMTT
```

I hope it helps you <3
