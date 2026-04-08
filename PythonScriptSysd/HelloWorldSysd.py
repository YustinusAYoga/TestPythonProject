#!/usr/bin/env python3
import time
import logging

# Set up logging to see output in systemd logs
logging.basicConfig(level=logging.INFO, format='%(message)s')

def main():
    while True:
        logging.info("Hello World from systemd!")
        time.sleep(10)  # Wait 10 seconds

if __name__ == "__main__":
    main()