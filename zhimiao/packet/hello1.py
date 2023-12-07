import subprocess


def tcpdump():
    p = subprocess.Popen('ls', stdout=subprocess.PIPE, encoding='utf-8')
    print(p.stdout.read())


tcpdump()
