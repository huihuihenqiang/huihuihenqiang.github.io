
# Git的使用技巧

author: ZH  |  date: 2023-11-24   |   category: Git

![机器学习](../../img/git.jpg)

## 将本地仓库上传到Github(第一次使用)

### 配置 Git

安装完成后，在开始菜单中找到 "Git" 文件夹，打开 "Git Bash"。在命令行中运行以下命令，设置你的用户名和邮箱：

```Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 验证安装

在安装完成后，你可以验证 Git 是否成功安装，以及查看版本号:

```git
git --version
```

如果成功安装，将显示 Git 的版本信息。

现在你已经成功安装了 Git，你可以在命令行中使用 Git 命令。例如，你可以使用 git clone 克隆仓库，使用 git add 添加文件，使用 git commit 提交更改等等。如果你需要更详细的帮助，可以使用 git --help 或查阅 Git 文档。

### 使用 Git 管理项目

打开 "Git Bash"，进入你的项目目录：

```git
cd /d/your/project/path
```

### 初始化仓库

使用 Git 在你的本地机器上初始化一个新的 Git 仓库 （如果你的项目还不是一个 Git 仓库）。

```git
git init
```

### 提交并推送代码

将你的博客代码提交到 GitHub 仓库

* 1 将项目文件添加到仓库：git add .
* 2 提交更改：git commit -m "Initial commit"
* 3 将本地仓库关联到 GitHub 上的远程仓库：git remote add origin <https://github.com/your-username/your-repository.git>
* 4 推送更改到 GitHub：git push -u origin master

现在，你的项目就被成功地推送到 GitHub 上的仓库中了。你可以在 GitHub 上的仓库页面上查看你的项目文件。你可以根据需要使用其他 Git 命令和 GitHub 功能来管理和协作你的项目。

```git
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<你的用户名>/<你的用户名>.github.io.git
git push -u origin master
```

---

### 如果已经初始化仓库

如果你已经初始化了 Git 仓库，并且在第一次提交后，下次提交需要执行以下几个步骤：

```git
git add .
这个命令将你项目中的所有更改添加到 Git 的暂存区，准备提交。

git commit -m "Your commit message here"
这个命令将暂存区中的更改提交到本地仓库，并附带一条提交信息，描述你所做的更改。

git push origin master
这个命令将你的本地更改推送到 GitHub 上的远程仓库。如果你在第一次推送时使用了 -u 选项，以后的推送可以简化为：
git push
```

这样，你就完成了一次提交并将更改推送到了远程仓库。在以后的每次修改后，只需重复上述步骤即可。记得及时提交并推送，以保持本地和远程仓库的同步。

### 怎么删除仓库里的某些文件

直接删除就行

### 优秀学习网站

1.廖雪峰-Git教程      [访问量: 30941698172，新手必看]<https://www.liaoxuefeng.com/wiki/896043488029600>
2.GitHub入门与实践 [密码:7aik，电子书，特别棒的入门书籍，2年后的感悟，强烈建议看这个]<https://wwc.lanzouo.com/i4BWko0gfje>
2.git-简明指南           [图形化模式，简单易懂]<https://rogerdudler.github.io/git-guide/index.zh.html>
3.图解Git                   [一样是图形化教程]<http://marklodato.github.io/visual-git-guide/index-zh-cn.html>
4.Git的奇技淫巧        [GitHub 14.9k stars]<https://github.com/521xueweihan/git-tips>
5.git-cheatsheeth      [图形化 Git 命令的作用域]<https://ndpsoftware.com/git-cheatsheet.html#loc=stas>

### 如何解决可能出现的网络连接问题

要设置代理什么的： <https://blog.csdn.net/m0_63230155/article/details/132070860>

在本地仓库修改之前，先从云端 git pull 一下，同步。

---

[上一页](#) | [下一页](#) | [返回主页](../../index.html)
