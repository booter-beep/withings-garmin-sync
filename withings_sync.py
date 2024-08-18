import os
import subprocess

def run_withings_sync():
    subprocess.run(["withings-sync", "-v"])

if __name__ == "__main__":
    run_withings_sync()
