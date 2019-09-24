[TOC]

# Git 入门

## 创建版本库

* **创建空目录**

	```
	mkdir learngit
	cd learngit
	pwd
	ls -ah -- 查看隐藏文件命令
	```

* **git init**

	`git init`

* **添加文件到版本库**

	1. *创建`readme.txt`文件* 	<!--需要放到learngit目录或子目录下-->

		Git is a version control system.
		Git is free software.

	2. *git add* 	<!--将文件添加到仓库-->

		`git add readme.txt`

	3. *git commit*	<!--添加提交说明，提交给仓库-->

		`git commit -m "wrote a readme file"`

* **总结**

	`commit`可以一次提交很多文件，所以你可以多次`add`不同的文件

	```
	git add file1.txt
	git add file2.txt file3.txt
	git commit -m "add 3 files."
	```

	

## 版本修改

* **修改`readme.txt`文件**

	Git is a distributed version control system.
	Git is free software.

* **git status**    <!--查看文件状态-->

	```
	$ git status
	On branch master
	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)
	      modified:   readme.txt
	no changes added to commit (use "git add" and/or "git commit -a")
	```

* **git diff**    <!--查看版本差异-->

	```shell
	$ git diff
	diff --git a/readme.txt b/readme.txt
	index d8036c1..013b5bc 100644
	--- a/readme.txt
	+++ b/readme.txt
	@@ -1,2 +1,2 @@
	-Git is a version control system.
	+Git is a distributed version control system.
	 Git is free software.
	\ No newline at end of file
	```

* **添加、查看状态、提交**

	```shell
	git add readme.txt
	git status
	git commit -m "add distributed"
	git status
	```

## 版本回退

* **多次修改`readme.txt`文件**

	Git is a distributed version control system.
	Git is free software distributed under the GPL.

* **提交**

	```
	git add readme.txt
	git commit -m "append GPL"
	```

* **git log**    <!--查看历史版本-->

	参数`--pretty=oneline`减少输出信息

	```
	git log
	git log --pretty=oneline
	```

* **git reset**    版本回退

	用`HEAD`表示当前版本，上一个版本就是`HEAD^`，往上100个版本写成`HEAD~100`

	`git reset --hard HEAD^`

	`cat readme.txt`

* **版本回到最新**    

	在不关闭命令行窗口时，可复制刚才的版本库的commit id(无需写全)，回到最新版本

	```
	git log
	git reset --hard 3a8e098eb35
	```

* **版本回到最新高级**

	命令`git reflog`用来记录你的每一次命令

	`git reflog`

## 暂存区

* **简单理解**

	所有`git add`提交修改的文件都在暂存区，`git commit`将暂存区内容提交到当前分支

* **修改`readme.txt`,增加`LICENSE`文本文件**

	Git is a distributed version control system.
	Git is free software distributed under the GPL.
	Git has a mutable index called stage.

* **查看状态**

	`git status`

* **添加**

	`git add readme.txt`

	`git add LICENSE`

	`git commit -m "understand how stage works"`

## 管理修改

* **简单理解**

	每次修改，都需要`git add`到暂存区，否则不会加入到`commit`中

* **查看当前版本库和工作区的区别**

	`git diff HEAD -- readme.txt`

	当工作区是clean（即暂存区的修改都已提交commit）时，工作区与当前最新版本库是一致的

## 撤销修改

* **简单理解**

	`git checkout -- file`可以撤销工作区的修改；`git reset HEAD <file>`可以把暂存区的修改撤销掉（unstage），重新放回工作区

## 删除文件

* **简单理解**

	删除文件也是一种修改。

* **确认 删除**

	`rm test.txt`

	`git status`

	`git rm test.txt`

	`git commit -m "remove test.txt"`

* **恢复删除**    未提交commit之前，若已提交则可以版本回退

	`git checkout -- test.txt`

	或者

	`git reset HEAD test.txt`

	`git checkout -- test.txt`

## 小总结

​	增删改均视为一次修改。

​	如果只在工作区修改，`git checkout -- file`可以撤销工作区的修改；如果`git add`后，`git reset HEAD <file>`可以把暂存区的修改撤销掉（unstage），重新放回工作区；如果`git commit`后，`git reset --hard HEAD^`或者`git reset --hard commitid`回退到某个版本。

## 添加远程仓库

- **准备工作**

	1. 创建ssh key

		`$ ssh-keygen -t rsa -C "youremail@example.com"`

	2. 登陆github，账户设置的ssh key中新增ssh key

	3. 创建新的仓库learngit

- **添加远程仓库**

	origin 为远程库的名称（默认叫法）

	`git remote add origin git@github.com:HsuHeinrich/learngit.git`

- **push本地仓库至远程**

	由于是第一次推送，加上-u参数（关联远程master分支）

	`git push -u origin master`

	以后本地库修改完成后就可以直接push

	`git push origin master`

## 克隆远程仓库

- **简单操作**

	`git clone git@github.com:HsuHeinrich/Heinrich-blog.git`

## 分支操作

- **参考廖雪峰网站**

	https://www.liaoxuefeng.com/wiki/896043488029600/896954848507552

## 其他操作

- **查看当前远程库信息**

	`git remote -v`

- **删除已有远程库**

	`git remote rm origin`

- **重新关联其他远程库**

	例如关联码云

	`git remote add origin git@gitee.com:yourname/learngit.git`

- 一个本地库关联多个远程库

	`git remote rm origin`

	`git remote add github git@github.com:yourname/learngit.git`

	`git remote add gitee git@gitee.com:yourname/learngit.git`

	