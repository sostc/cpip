from deva.pipe import *
from deva.stream import Stream
import dill
import time
import requests

def install(lib_name):
    install_command = 'pip install --no-cache --force-reinstall -i https://pypi.tuna.tsinghua.edu.cn/simple/ %s'%(lib_name)
    test_command = """python3 -c 'import %s;print("installed:" ,%s.__version__)'"""%(lib_name,lib_name)
    
    command = install_command+'\n'+test_command
    install_ps = Stream.from_command(command)
    irl = install_ps.map(lambda x:x>>stdout).sink_to_list()
  
    install_ps.subp.wait()

    
    requests.post('http://518.is:9990',data=irl>>concat(''))
    
    'finished'>>to_print
    

import argparse
  
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--libname", required=True,
    help="path to the input image")
args = vars(ap.parse_args())


install(args["libname"])