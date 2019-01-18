# -*- coding:utf-8 -*-

import subprocess
from urllib import request, parse
import sys
import json

def setup(tel, lib_name):
    '''开始安装'''
    install_command = "pip install -i {source} --force-reinstall --ignore-installed --no-cache-dir {lib_name}"
    test_command = 'python -c "import %s;print("""test_installed:""",%s.__version__)"'%(lib_name,lib_name)
    command = install_command + "&&" + test_command
    source = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    lib_name = lib_name
    # 执行命令 获取输出
    p = subprocess.Popen(command.format(source=source, lib_name=lib_name), 
                         shell=True, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         )
    
    info = ""
    for out in p.stdout:
        out = out.decode("utf-8")
        print(out)
        info += out
    
    p.wait()


    # post
    url = "http://518.is:9990"
    data = {
        "tel": tel,
        "info": info,
    }
    
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, data=data) 
    try:
        request.urlopen(req)
    except:
        pass



if __name__ == "__main__":
    if len(sys.argv) == 1:
        lib_name = None
        while not lib_name:
            lib_name = input("输入安装的库名：")
        tel = input("输入收货人联系手机号：") 
        setup(tel, lib_name)

    elif len(sys.argv) == 2:
        lib_name = sys.argv[1]
        tel = "518"
        setup(tel, lib_name)

    else:
        print("help")
        sys.exit()

    