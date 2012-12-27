#重定向到标准错误输出

	>&2 #&-->'the same as' 报错信息的处理，为了让错误信息更鲜明

#查看命令执行的返回值

	echo $?  #返回0 成功，非0 失败

#wildcard(通配符)
You can use wildcards with any command that accepts filename arguments.
## ?
Matches any single character

	Data??? #followed by exactly 3 more characters

## [!characters]
Matches any character that is not a member of the set characters

## [characters]
Matches any character that is a menber of the set characters

	[abc]* #Any filename that begins with "a" or "b" or "c" followed by any other characters 

	[[:upper:]]* #Any filename that begins with an uppercase letter.

	BACKUP.[[:digit:]][[:digit:]]  #Followed by exactly two numerals

	*[![:lower:]] #Any filename that does not end with a lowercase letter.

#What are commands?
Commands can be one of 4 different kinds:

##An excutable program
Like all files that we saw in /usr/bin. 

##A command built in the the shell itself
Bash provides a number of commands internally called shell builtins, The cd command.

##A shell function
they exist

##An alias
Commands that you can define yourselves,built form other commands
#shell command
##less 
For text files use less to view them
	less shi.txt

## cp, mv, rm, mkdir

	cp -i -R    #interactive recursive (互动，递归)
	mv -i
	rm -i -r

	rm *~       #Some applications create backup files using this naming scheme. clean them.

## type, which, man, help

	type    #display the kind of command the shell will execute, given a particular command name.
	which   #To determine the exact location of a given executable.
	man , help #getting command documentionshi

