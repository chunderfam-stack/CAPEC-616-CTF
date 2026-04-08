import time
import signal
import sys

def handle_exit(signum, frame):
    print("\n[!] Rogue process terminated!", flush=True)
    sys.exit(0)

# Catch termination signals
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)  # Ctrl+C

print("[*] Rogue process running...", flush=True)

while True:
    time.sleep(2)
