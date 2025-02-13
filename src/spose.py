#!/usr/bin/env python3

import sys
import argparse
import urllib.request
from colorama import Fore, Style, init

from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize colorama for color support
init(autoreset=True)

class Spose:
    executor = ThreadPoolExecutor(max_workers=16)
    all_task = []

    def scan_port(self, target, port):

        # Set up proxy
        proxy_handler = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

        try:
            url = f"http://{target}:{port}"
            with urllib.request.urlopen(url) as response:
                code = response.getcode()
                if code in [200, 404, 401]:
                    print(f"{Fore.GREEN}{target}:{port} seems OPEN{Style.RESET_ALL}")
        except urllib.error.HTTPError as e:
            # Suppress output for HTTP errors
            if e.code in [503]:
                return
        except urllib.error.URLError:
            # Suppress output for URL errors
            return
        except Exception:
            # Suppress output for all other exceptions
            return

    def __init__(self):
        parser = argparse.ArgumentParser(
            add_help=True,
            description='Squid Pivoting Open Port Scanner (Support Thread)'
        )
        parser.add_argument("--proxy", help="Define proxy address URL (http://x.x.x.x:3128)",
                            action="store", dest='proxy', required=True)
        parser.add_argument("--target", help="Define target IP behind proxy",
                            action="store", dest='target', required=True)
        parser.add_argument("--ports", help="[Optional] Define target ports behind proxy (comma-separated)",
                            action="store", dest='ports')
        parser.add_argument("--allports", help="[Optional] Scan all 65535 TCP ports behind proxy",
                            action="store_true", dest='allports')
        parser.add_argument("--threads", help="[Optional] Define number of threads, default is 16",
                            action="store", dest='threads', default=16, type=int)

        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        
        options = parser.parse_args()

        self.target = options.target
        self.proxy = options.proxy
        
        self.executor = ThreadPoolExecutor(max_workers=options.threads)

        # Determine the list of ports to scan
        if options.allports:
            ports = range(1, 65536)  # All TCP ports
            print(f"{Fore.YELLOW}Scanning all 65,535 TCP ports{Style.RESET_ALL}")
        elif options.ports:
            ports = [int(port.strip()) for port in options.ports.split(",")]
            print(f"{Fore.YELLOW}Scanning specified ports: {options.ports}{Style.RESET_ALL}")
        else:
            ports = [21, 22, 23, 25, 53, 69, 80, 109, 110, 123, 137, 138, 139, 143, 156, 389, 443,
                     546, 547, 995, 993, 2086, 2087, 2082, 2083, 3306, 8080, 8443, 10000]
            print(f"{Fore.YELLOW}Scanning default common ports{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Using proxy address {self.proxy}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Threads number {options.threads} {Style.RESET_ALL}")

        # Scan the ports
        for port in ports:
            self.all_task.append(self.executor.submit(self.scan_port, self.target, port))

        for future in as_completed(self.all_task):
            future.result()

        print("[*] Done !")

def main_function():
    Spose()

if __name__ == "__main__":
    main_function()
