import os
import subprocess

def main():
    if os.geteuid() != 0:
        print("This script requires superuser access.")
        print("Restarting the script with sudo...")
        
        subprocess.call(['sudo', 'python3', __file__])
        return

    import main as archdroid_main
    archdroid_main.run()

if __name__ == "__main__":
    main()