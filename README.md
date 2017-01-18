# 安卓批量签名工具使用说明

## 安卓批量签名工具使用Python编写，利用此工具对未签名apk实现修改AndroidManifest.xml的多个meta-data信息，并自动签名（可实现多个签名）
## 如果只需要进行多渠道打包，可参考：[Android多渠道打包工具][1]

## 一、目录及使用说明
### sign_start：Mac下签名执行程序，双击执行  
sign_start.bat：Window下签名执行程序，双击执行  
unsigned.apk：待签名的apk  
my.keystore：签名文件  
out文件夹（程序执行后创建）：签名好的apk存放目录  
log文件夹（程序执行后创建）：日志文件存放目录

## 二、使用前准备工作
### 1、检查环境
(1),python环境检查：Windows/Mac：cmd/终端下输入python，如果有输出版本号，则说明已安装，推荐版本python2.7  
下载地址：https://www.python.org/downloads/release/python-2712/  
（2），jdk环境检查：Windows/Mac：cmd/终端下输入python，如果有输出版本号，则说明已安装，推荐版本1.7  
下载地址：http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html  

2、安装Simplejson  
Windows参考：http://www.cnblogs.com/kaituorensheng/archive/2012/07/25/2608864.html  
Mac参考：https://site.douban.com/129642/widget/notes/5513129/note/388411666/  

上述步骤做完后可执行sign_start.bat(Windows)或sign_start(Mac)程序测试，如果out输出qihu360_signed.apk与wandoujia_  signed.apk并且可安装，则说明环境配置成功  

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

## 三、注意事项：
### 1、Windows请AndroidSignTool放在D盘根目录下！
2、建议使用jdk1.7，jdk1.6可能出现无法签名的情况

## 有任何问题请在简书留言：[http://www.jianshu.com/p/b1b549010404][2]

[1]: https://github.com/skynewborn/android-multichannel-packaging-tool
[2]: http://www.jianshu.com/p/b1b549010404