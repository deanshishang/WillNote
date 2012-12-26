#重定向到标准错误输出

	>&2 #&-->'the same as' 报错信息的处理，为了让错误信息更鲜明

#查看命令执行的返回值

	echo $?  #返回0 成功，非0 失败

#shell command
##less 
For text files use less to view them
	less shi.txt
