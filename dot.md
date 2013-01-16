#2012/12/12
##django:
blank=true 字段可以不填写
null=true 数据库中将此字段设置为NULL
unique=true 字段唯一值

使用Fabric部署网站应用 --- >郭哥推荐 Akill群聊天记录


#2012/12/14
##python
Pyhon Imaging Library http://www.pythonware.com/products/pil/index.htm 库的安装： error: command 'gcc' failed with exit status 1 -----> 依赖于python-devel,需提前安装

fedora 桌面环境gnome和kde，前者 sudo yum install gconf-editor gnome-tweak-tool;
 修改advace setting中的Desktop /usr/share/application 中是各种应用程序，复制到桌面即可;
 修改system setting中的键盘中的快捷方式，自己手动添加。


#2012/12/17
##tmux
tmux安装使用，web开发了解分类，前端开发后台开发。
.tmux.conf 配置文件

	unbind C-b
	set -g prefix C-a
	setw -g mode-keys vi

	# split window like vim
	# vim's defination of a horizontal/vertical split is revised from tumx's
	bind s split-window -h
	bind v split-window -v
	# move arount panes wiht hjkl, as one would in vim after C-w
	bind h select-pane -L
	bind j select-pane -D
	bind k select-pane -U
	bind l select-pane -R

	# resize panes like vim
	# feel free to change the "1" to however many lines you want to resize by,
	# only one at a time can be slow
	bind < resize-pane -L 10
	bind > resize-pane -R 10
	bind - resize-pane -D 10
	bind + resize-pane -U 10

	# bind : to command-prompt like vim
	# this is the default in tmux already
	bind : command-prompt

##Gnome-terminal 的技巧，peter视频

	/bin/godean-->gmome-teminal --full--screen --hide-menubar  
	sudo chmod 775 godean

#2012/12/18
##dd
urldispatch orm 见本子上笔记
网站开发：css margin,padding,border,background...   
郭哥讲得viptime开发流程分工

##eryaeat的管理界面设计，桌子信息，点击出现单子列表，左下角呼叫刷新界面，右边是实施上菜信息。
##peter--chrome-development happycast视频

#2012/12/19
##google-chrome安装,需要sudo yum lsb 

#2012/12/24
##django 文档
django queryset

#2012/12/25
perter bash-script 视频

#2012/12/27
learn shell command 

#2013/01-03 
沈阳 全子 马子 隋头聚会

#2013/01/08
接口讨论 进行代码编写

#2013/01/16
在django的model中，pk的值大小不一定和表中自己设置的序列号一样。chidianer.order.views 中docontrast部分出现错误
