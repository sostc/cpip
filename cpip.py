<<<<<<< HEAD
# -*- coding:utf-8 -*-

import subprocess
from urllib import request, parse
import sys
import json

def get_env():
    p = subprocess.Popen("python -V", 
                         shell=True, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         )
    res = p.stdout.read().decode('utf-8',errors='ignore')
    py_version = res.split()[1]
    path = sys.path
    return {"py_version":py_version, "path":path}





# 生成命令
def gen_command(lib_name):
    # 检测python版本
    env = get_env()
    py_version = env.get("py_version")

    source = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    install_command = "pip install -i {source} --force-reinstall --ignore-installed --no-cache-dir {lib_name}".format(source=source, lib_name=lib_name)
    

    # 如果是python3.7 并且lib_name是tensorflow，单独定义安装方式
    if py_version.startswith("3.7") and lib_name.lower() == "tensorflow":
        install_command = "pip install https://download.lfd.uci.edu/pythonlibs/r5uhg2lo/tensorflow-1.9.0-cp37-cp37m-win_amd64.whl"
    # 如果lib_name是tensorflow 降低依赖库版本
    if lib_name.lower() == "tensorflow":
        install_command = install_command + "&&" + "pip install protobuf==3.6.0"

    test_command = 'python -c "import %s;print("""test_installed:""",%s.__version__)"'%(lib_name,lib_name)
    command = install_command + "&&" + test_command

    return command


def setup(tel, lib_name):
    '''开始安装'''
    
    command = gen_command(lib_name)
    # 执行命令 获取输出
    p = subprocess.Popen(command, 
                         shell=True, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         )
    
    info = ""
    for out in p.stdout:
        out = out.decode("utf-8", errors='ignore')
        print(out)
        info += out
    
    p.wait()


    # post
    url = "http://518.is:9990"
    data = {
        "tel": tel,
        "lib_name":lib_name,
        "info": info
    }
    
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, data=data) 
    try:
        request.urlopen(req)
    except:
        pass

    input("输入回车退出程序")

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

=======
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

>>>>>>> 6d2b95d05fa7872ab8b556602283e5358d779c9a
    