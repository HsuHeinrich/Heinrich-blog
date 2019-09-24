## 添加远程仓库

* **准备工作**

  1. 创建ssh key

     `$ ssh-keygen -t rsa -C "youremail@example.com"`

  2. 登陆github，账户设置的ssh key中新增ssh key
  3. 创建新的仓库learngit

* **添加远程仓库**

  origin 为远程库的名称（默认叫法）

  `git remote add origin git@github.com:HsuHeinrich/learngit.git`

* **push本地仓库至远程**

  由于是第一次推送，加上-u参数（关联远程master分支）

  `git push -u origin master`

  以后本地库修改完成后就可以直接push

  `git push origin master`

## 克隆远程仓库

* **简单操作**

  `git clone git@github.com:HsuHeinrich/Heinrich-blog.git`

## 分支操作

* **参考廖雪峰网站**

  https://www.liaoxuefeng.com/wiki/896043488029600/896954848507552

## 其他操作

* **查看当前远程库信息**

  `git remote -v`

* **删除已有远程库**

  `git remote rm origin`

* **重新关联其他远程库**

  例如关联码云

  `git remote add origin git@gitee.com:yourname/learngit.git`

* 一个本地库关联多个远程库

  `git remote rm origin`

  `git remote add github git@github.com:yourname/learngit.git`

  `git remote add gitee git@gitee.com:yourname/learngit.git`

  