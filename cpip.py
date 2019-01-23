# -*- coding:utf-8 -*-

import subprocess
from urllib import request, parse
import sys
import json
import platform


def get_env():
    p = subprocess.Popen("python -V", 
                         shell=True, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         )
    res = p.stdout.read().decode('utf-8',errors='ignore')
    py_version = res.split()[1]
    path = sys.path
    os = platform.platform()
    return {"py_version":py_version, "path":path,'os':os}


# 生成命令
def gen_command(lib_name):
    # 检测python版本
    env = get_env()
    py_version = env.get("py_version")
    os = env.get('os')
    error_msg = ''
    

    source = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    install_command = "pip install -i {source} --force-reinstall --ignore-installed --no-cache-dir {lib_name}".format(source=source, lib_name=lib_name)
    
    if os.startswith('Windows'):
        connect_str = "&&"
    else:
        connect_str = ";"

    # 如果是python3.7 并且lib_name是tensorflow，单独定义安装方式
    if py_version.startswith("3.7") and lib_name.lower() == "tensorflow":
        if os.startswith('Windows'):
            install_command = "pip install https://download.lfd.uci.edu/pythonlibs/r5uhg2lo/tensorflow-1.9.0-cp37-cp37m-win_amd64.whl"
        else:
            install_conmand = None
            error_msg = 'not windows ,can not install tensorflow in py3.7'
            print(error_msg)
            return None,error_msg
    # 如果lib_name是tensorflow 降低依赖库版本
    if lib_name.lower() == "tensorflow":
        iinstall_command = install_command + connect_str + "pip install protobuf==3.6.0"
        
        

    test_command = 'python -c "import %s;print("""test_installed:""",%s.__version__)"'%(lib_name,lib_name)
    install_command = install_command + connect_str + "pip install protobuf==3.6.0"
    command = install_command + connect_str + test_command


    return command,error_msg


def setup(tel, lib_name):
    '''开始安装'''
    
    command,error_msg = gen_command(lib_name)
    if command:
        info = ''
        p = subprocess.Popen(command, 
                         shell=True, 
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT
                         )
                         
        for out in p.stdout:
            out = out.decode("utf-8", errors='ignore')
            print(out)
            info += out
            
        p.wait()
        
    else:
        info = error_msg
    post_log(tel,lib_name,info)


def post_log(tel,lib_name,info):    # post
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

def verify(tel):
    url = "http://518.is:9991/verify/%s"%tel
    req = request.Request(url)
    resp = request.urlopen(req)
    if int(resp.read().decode('utf-8')):
        return 1
    else:
        return 0
    
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        lib_name = None
        while not lib_name:
            lib_name = input("输入安装的库名：")
        tel = input("输入收货人联系手机号：") 
        
        if verify(tel):
            setup(tel, lib_name)
        else:
            print('请将收货手机号码发给卖家，获取程序使用权限')

    elif len(sys.argv) == 2:
        lib_name = sys.argv[1]
        tel = "518"
        setup(tel, lib_name)

    else:
        print("help")
        sys.exit()



    