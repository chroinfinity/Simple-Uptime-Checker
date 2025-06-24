import subprocess

timeout = 2
host = "www.google.com"

result = subprocess.run(
            ['ping', '-c', '1', '-W', str(timeout), host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

print(result.returncode)