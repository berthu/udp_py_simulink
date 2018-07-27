import multiprocessing 
import subprocess

def worker(file):
    subprocess.Popen(['python', file])

if __name__ == "__main__": 
    files = ['udp_send.py', 'udp_receive.py', 'udp_receive2.py']
    for i in files: 
        p = multiprocessing.Process(target = worker(i))
        p.start()
    while True:
        pass
        
