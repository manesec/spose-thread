# Spose

Squid Pivoting Open Port Scanner

mode by @manesec, add threading support and setup.py.

Detecting open port behind squid proxy for CTF and pentest purpose using http proxy method. Only for Python 3 version.

## Install & Usage

```
$ pipx install git+https://github.com/manesec/spose-thread

$ spose --help
```

## Manual way

```
❯ python3 ./spose.py --help
usage: spose.py [-h] --proxy PROXY --target TARGET [--ports PORTS] [--allports]

Squid Pivoting Open Port Scanner

options:
  -h, --help       show this help message and exit
  --proxy PROXY    Define proxy address URL (http://x.x.x.x:3128)
  --target TARGET  Define target IP behind proxy
  --ports PORTS    [Optional] Define target ports behind proxy (comma-separated)
  --allports       [Optional] Scan all 65535 TCP ports behind proxy
```

## VulnHub VM

- sickOS 1.1
- pinkys-palace

## References

- https://github.com/manesec/spose-thread
- https://www.rapid7.com/db/modules/auxiliary/scanner/http/squid_pivot_scanning

## License

This program is under MIT License.