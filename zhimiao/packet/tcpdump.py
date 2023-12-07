import sys
import time
import datetime


class TcpDumpUtils():
    def __init__(self, dumpName='./log/', arguments=None):
        self.dumpFilePath = dumpName
        self.fileName = 'test'
        if arguments is not None:
            for argob in arguments:
                if arguments[argob] is True:
                    self.fileName += str(argob) + '_'
        ####随机产生一个时间戳
        startTime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        self.fileName += startTime + ".pcag"

    ####开启抓包
    def startTcpdumpWithFile(self):
        import subprocess
        # p = subprocess.Popen('tcpdump -i any -s 0 tcp -w ./ding.pcapng', shell=True)
        cmd1 = ['tcpdump', '-i', 'any', '-s', '0', 'tcp', '-w', self.dumpFilePath + self.fileName]
        self.tcpprocess = subprocess.Popen(cmd1)
        return self.tcpprocess

    ####停止抓包
    def stopTcpdumpWithFile(self):
        time.sleep(2)
        self.tcpprocess.kill()

    def tcpdump(self):
        import subprocess, fcntl, os
        # sudo tcpdump -i eth0 -n -s 0 -w - | grep -a -o -E "Host: .*|GET /.*"
        cmd1 = ['sudo', 'tcpdump', '-i', 'en0', '-n', '-B', '4096', '-s', '0', '-w', '-']
        cmd2 = ['grep', '--line-buffered', '-a', '-o', '-E', 'Host: .*|GET /.*']
        p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stdin=p1.stdout)
        flags = fcntl.fcntl(p2.stdout.fileno(), fcntl.F_GETFL)
        fcntl.fcntl(p2.stdout.fileno(), fcntl.F_SETFL, (flags | os.O_NDELAY | os.O_NONBLOCK))
        return p2

    @staticmethod
    def poll_tcpdump(proc):
        # print 'poll_tcpdump....'
        import select
        txt = None
        while True:
            # wait 1/10 second
            readReady, _, _ = select.select([proc.stdout.fileno()], [], [], 0.1)
            if not len(readReady):
                break
            try:
                for line in iter(proc.stdout.readline, ""):
                    if txt is None:
                        txt = ''
                    txt += str(line)
            except IOError:
                print
                'data empty...'
                pass
            break
        return txt


