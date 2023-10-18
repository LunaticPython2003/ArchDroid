def get_kernel():
    kernel_release = subprocess.check_output(['uname', '-r']).decode('utf-8').strip()
    if 'xanmod' in kernel_release or 'zem' in kernel_release:
        return 1
    else:
        return 0

def ensure_kernel():
    os.system("sudo pacman -S xanmod")