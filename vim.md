*cw--->替换从光标所在位置后到一个单词结尾的字符

*0---->到行首

*^---->到第一个不是blank的地方

*$---->到行尾

*g_--->到行尾不是blank的地方

*saveas---->另存为

*100 i desu ECS ----> 打印100个desu

*.--->重复上个命令

*NG---->跳到第n行

*w----->到下一个单词的开头

*e----->到当前单词的结尾

*%----->匹配括号移动

*#----->匹配光标到上一个匹配的单词

**----->匹配光标到下一个匹配的单词

*<start option><command><end position>

	0,y,$ 先到行头，开始复制操作到行尾
	
	ye 从当前位置复制到本单词的结尾

*gu,gU 变大小写

*fa ---->找到下一个a字符

*t, ---->跳到下一个,之前的字符处

*3fa --->在当前行跳到第三个a地方

*va( --->选择包含(的括号内的内容 <action>a<object>

*vi( --->选择()之间的内容 不包含() <action>i<object>

*v2a( --->选择两个括号之间的内容包括括号
