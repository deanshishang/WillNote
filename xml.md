可扩展标记性语言  XML 用来结构化文档和数据的通用而且适用性强的格式，传输与存储数据。
为了传输数据，而不是显示数据，需要自定义标签，具有自我描述性
XML 为了传输，焦点是数据的内容；HTML 为了显示，焦点是数据的外观；

结构化，存储和传输信息；

没有任何行为，仅仅是纯文本，标签的功能性意义依赖于应用程序的特性；

是HTML的补充，而不是替代；

是独立于软件和硬件的信息传输工具；

信息存储和描述领域越来越流行；

把数据从HTML分离出来；单独进行存储和分享；专注于HTML进行布局；

可以在不兼容的系统上进行交换数据；

根元素与子元素；根元素必须有；跟元素是其他所有元素的父元素；

XML中必须要有关闭标签；

标签大小写敏感；

XML的属性值必须加上引号；

实体引用，比如< 是不能单独出现的，用实体引用符号来代替：&lt; &gt 大于; &amp &; &apos '; &quot ";

XML中，空格会被保留；

XML 以LF存储换行；

XML在不中断应用程序的情况下可以进行扩展；

属性通常提供不属于数据组成部分的信息，属性中文件类型与数据本身无关，但是对需要处理这个元素的软件来说却很重要；

XML中的元素 VS 属性：

<person sex="female"> <sex>female</sex>  第一个例子中sex是属性，第二个中书元素，两个例子均可以提供相同的信息；但是，XML中尽量避免使用属性，如果看起来像数据，那么就用子元素吧。


最喜欢的方式排序：
<note date="08/08/2008"></note>
<note><date>08/08/2008</date></note>
<note><date><day>08</day><month>08</month><year>2008</year></date></note>

仅仅使用属性来提供与数据无关的信息；

有关数据的数据即元数据应当存储为属性，而数据本身应当存储为元素。


用CSS显示XML,但是不推荐，还是用XSLT来格式化XML，是XML首选的XML样式表语言;


XML JavaScript:

XMLHttpRequest用于在后台与服务器进行交换数据；

作用：不重新加载界面的情况下局部刷新；在页面记载之后进行请求和接受数据；在后台向服务器发送数据；

XML DOM：文档对象模型，DOM将XML作为一个树形结构，而树叶被定义为节点；定义了访问XML的标准，是一个使一个程序或者脚本能工动态的访问和更新文档的内容，结构以及样式的平台和语言中立的接口；是用于获取，更改，添加或者删除XML元素的标准；

通过DOM树来访问所有元素，可以修改或者删除他们的内容，并且创建心的元素，元素，他们的文本，以及属性，都被认为是节点。

XML DOM
xmlDoc.getElementsByTagName("to")[0].childNodes[0].nodeValue
xmlDoc 是由解析器创建的XML文档，getElementsByTagName("to")[0]是获取第一个to元素，childNodes[0]是获取元素的第一个子元素，nodeValue是元素的值，即节点的值；

HTML DOM
document.getElementById("to").innerHTML=
document是HTML文档，getElementById("to")其中id=“to”的元素，innerHTML元素的内部文本

XML应用程序
由HTML和JAVASCRIPT构建一个小型的XML应用程序ZZZZ
