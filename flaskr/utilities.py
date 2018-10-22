import subprocess

def ping_device(device_addr):
    ping_response = subprocess.Popen(["/sbin/ping", "-c1", "-w1", device_addr], stdout=subprocess.PIPE)
    ping_response.wait()
    print(ping_response.returncode)


