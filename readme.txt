
========安卓批量签名工具使用说明========

一、目录及使用说明
sign_start：Mac下签名执行程序，双击执行
sign_start.bat：Window下签名执行程序，双击执行
unsigned.apk：待签名的apk
my.keystore：签名文件
out文件夹（程序执行后创建）：签名好的apk存放目录
log文件夹（程序执行后创建）：日志文件存放目录

二、使用前准备工作
1、检查环境
(1),python环境检查：Windows/Mac：cmd/终端下输入python，如果有输出版本号，则说明已安装，推荐版本python2.7
下载地址：https://www.python.org/downloads/release/python-2712/
（2），jdk环境检查：Windows/Mac：cmd/终端下输入python，如果有输出版本号，则说明已安装，推荐版本1.7
下载地址：http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html

2、安装Simplejson
Windows参考：http://www.cnblogs.com/kaituorensheng/archive/2012/07/25/2608864.html
Mac参考：https://site.douban.com/129642/widget/notes/5513129/note/388411666/

上述步骤做完后可执行sign_start.bat(Windows)或sign_start(Mac)程序测试，如果out输出qihu360_signed.apk与wandoujia_signed.apk并且可安装，则说明环境配置成功

3、准备签名配置文件
格式参考本目录下的sign_info.txt（命名不变，替换内容即可），文件为标准son格式，字段说明如下：
type：渠道名称（缺省字段，暂未用到）
targetApk：目标包名（打包后的apk名）
keystoreName: 签名文件名称
keystorePassword：签名文件密码
keystoreAlias：签名文件别名
replace：替换的内容集合（注：目前只支持替换AndroidManifest.xml下的meta-data字段），字段说明如下：
android:name：需要替换的名称(用于查找，名称本身不被替换)
android:value：需要替换的内容

4、将待签名的apk重命名为unsigned.apk，替换当前目录下的同名文件

5、将签名文件重命名为my.keystore，替换当前目录下的同名文件
签名文件密码配置：使用文本工具打开目录下的sign_win.py(Window)或sign.py(Mac)文件，将81行的文本”123456“替换为你的密码

三、注意事项：
1、Windows请AndroidSignTool放在D盘根目录下！
2、建议使用jdk1.7，jdk1.6可能出现无法签名的情况
3、有任何问题请联系我（QQ：610864358）



