# cpip
朝天吼python库安装工具

## 使用方式
### windows
直接执行 cpip
或者cpip libname



##针对所有包
pip freeze > requirements.txt
　　然后通过以下命令来安装 dependency:
pip install -r requirements.txt
　　
## 针对固定某个目录
先安装pipreqs
pip install pipreqs

在目标目录下执行
pipreqs ./

然后通过以下命令来安装 dependency:

pip install -r requirements.txt