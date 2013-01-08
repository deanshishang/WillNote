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

#I/O Redirection
By using some special notations we can redirect the output of many commands to files, devices, and even to the input of other commands
##Standard Output

	ls > file_list.txt   #overwritten

	ls >>file_list.txt   #appednded

##Standard Input
By default, standard input gets its contents from the keyboard,But like standard output, it can be redirected, < 

	sort < file_list.txt #process the contents of file_list.txt. The results are output on the display since the standard output was not redirected

	sort < file_list.txt > file_new_list.txt #redirected standard output to another file like this

A command can have both its input and output redirected, Be aware that the order of the redirection does not matter. The only requirement is that the redirection operators(< >) must appear after the other options and arguments in the command.

##Piplines
The most powerful and useful thing you can do with I/O redirection is to connect multiple commands together with what are called pipelines, the standard output of one command is fet(送出) into the standard input of another.Here is my absolute favorite:

	#ls -l | less #the output of the ls command is fed into less, 

You can make any command have scrolling output, I use this technique all the time.

	#ls -lt | head
	#du | sort -nr
	#find . -type f -print | wc -l

##Filters
One kind of program frequently used in pipelines is called filters. Filters take a standard input and perform an operation upon it and send the results to standard output. In this way, they can be combined to process information in powerful ways, act as filters.

	sort  #sorts standard input then outputs the sorted result on standard output.
	uniq  #given a sorted stream of data from standard input, it removes duplicate lines of data, it make sure that every line is unique
	grep  #Examines each line of data it recerves from standard input and out puts every line that contains a specified pattern of characters
	fmt   #formatted text on standard output
	pr    #split the data into pages with page breaks,headers and footers in preparation for printing.
	head  #outputs the first few lines of its input. Useful for getting the header of a file
	tail  #the last few lines of its input.getting the most recent entries from a log file
