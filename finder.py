
from lib.controllers import Controller
from lib.arguments import parse_args
import multiprocessing, requests, time
fe = open("proxies.txt", "a")
be = open("proxies.txt", "r")

def scrape():
  global fe, be
  be.truncate(0)
  be.close()
  r = requests.get('https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http%2Bs.txt')
  x = r.text
  fe.write(x)
  fe.close()

if __name__ == "__main__":
    scrape()
    time.sleep(1)
    multiprocessing.freeze_support()
    controller = Controller(
        arguments=parse_args()
    )
    try:
        controller.join_workers()
    except KeyboardInterrupt:
        pass
        
