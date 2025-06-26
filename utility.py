import subprocess

timeout = 2
host = "www.google.com"

def ping_request(host, timeout):
    result = subprocess.run(
                ['ping', '-c', '1', '-W', str(timeout), host],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
    return result

print(ping_request(host, timeout))