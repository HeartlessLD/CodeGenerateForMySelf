
##个人用的代码生成工具
通过简单的配置命令 通过模板自动生成文本代码

使用前请安装python2.7

##使用方法
先配置好模板文件，参照template.h template.cpp


现在支持的命令参数有${author} ${time} ${param0} ${param1}...个数取决于命令参数的个数

使用脚本 例子：./test.py FileName param0 param1 param2
