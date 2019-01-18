# cpip
朝天吼python库安装工具

## 使用方式
### windows
直接执行 
cpip
或者
cpip libname



##针对所有包
`pip freeze > requirements.txt`
　　然后通过以下命令来安装 dependency:
`pip install -r requirements.txt`　　
## 针对固定某个目录
- 先安装pipreqs
`pip install pipreqs`

- 在目标目录下执行

`pipreqs ./`

然后通过以下命令来安装 dependency:

`pip install -r requirements.txt`

## git 教程
### 新建分支

`git checkout -b dayuseonly`

相当于执行了

`git branch iss53
git checkout iss53`

### 切换分支 

`git checkout master`

Switched to branch 'master'
### 其他
查看项目的分支们 (包括本地和远程)

`git branch -a`


#### 删除本地分支
`git branch -d <BranchName>`



#### 删除远程分支
`git push origin --delete <BranchName>`


#### 查看删除后分支们
`git branch -a`
