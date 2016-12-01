#!/usr/bin/env python
#coding:utf-8
import re
import os
import sys
import simplejson as json
import time
import shutil
import platform

curpath = sys.path[0]
print("===log===当前路径: %s" % curpath)
curtime = time.time()
ISOTIMEFORMAT = '%Y-%m-%d %X'

curtime = time.strftime(ISOTIMEFORMAT,time.gmtime(time.time()))
print("===log===当前时间: %s" % curtime)

# 解包后的文件夹路径
unsignedFilesPath = "%s/unsigned" % curpath

# 判断out文件夹和log文件夹是否存在，不存在则创建
outFileIsExist = os.path.exists('%s/unsigned' % curpath)
if not outFileIsExist:
	# 创建文件夹
	os.mkdir('%s/out' % curpath)

logFileIsExist = os.path.exists('%s/log' % curpath)
if not logFileIsExist:
	# 创建文件交
	os.mkdir('%s/log' % curpath)

# 日志文件
logFile = open('log/sign_log%s.txt' % curtime,'w')
errorFile = open('log/error_log.txt%s' % curtime,'w')
errorFile.write("打包失败的targetApk：\n")

# 0, 判断解包文件夹是否存在，存在则删除
fileIsExist = os.path.exists('%s/unsigned' % curpath)
if fileIsExist:
	# 删除文件夹
	shutil.rmtree('%s/unsigned' % curpath)

# 1，反编译
apktoolDStartLog = '===log===正在反编译……'
print(apktoolDStartLog)
logFile.write(apktoolDStartLog + '\n')
r = os.system('apktool d %s/unsigned.apk -o %s/unsigned' % (curpath,curpath))
apktoolDEndLog = '===log===反编译结果：%s' % r
print(apktoolDEndLog)
logFile.write(apktoolDEndLog + '\n')

# 签名函数
def signTask(signInfo):
	# 2, 修改AndroidManifest.xml
	replaceInfos = signInfo["replace"]
	for replaceInfo in replaceInfos:
		print('===log===replaceInfo:')
		print('===log===android:name:' + replaceInfo["android:name"])
		print('===log===android:value:' + replaceInfo["android:value"])
		# 打开文件
		androidManifest=open('%s/AndroidManifest.xml' % unsignedFilesPath,'r+')
		androidManifestLines=androidManifest.readlines()
		# 浏览行
		for index,li in enumerate(androidManifestLines):
			# 查找文本
			replaceStr = 'android:name="%s"' % replaceInfo["android:name"]
			if replaceStr in li:
				# 替换行
				li = '\t\t<meta-data android:name="%s" android:value="%s"/>\n' % (replaceInfo["android:name"],replaceInfo["android:value"])
				androidManifestLines[index] = li
				replaceLog = '===log===文本"%s"替换成功' % replaceStr
				print(replaceLog)
				logFile.write(replaceLog + '\n')
		androidManifest=open('%s/AndroidManifest.xml' % unsignedFilesPath,'w+')
		androidManifest.writelines(androidManifestLines)
	androidManifest.close()

	# 3, 回编译
	apktoolBStartLog = '===log===正在回编译……'
	print(apktoolBStartLog)
	logFile.write(apktoolBStartLog + '\n')
	r2 = os.system('apktool b %s/unsigned' % curpath)
	apktoolBEndLog = '===log===回编译结果：%s' % r2
	print(apktoolBEndLog)
	logFile.write(apktoolBEndLog + '\n')

	# 4，签名
	r3 = 1
	if r2 == 0:
		r3 = os.system('jarsigner -sigalg MD5withRSA -digestalg SHA1 -keystore %s/%s -storepass %s -signedjar %s/out/%s.apk %s/unsigned/dist/unsigned.apk %s' % (curpath,signInfo["keystoreName"],signInfo["keystorePassword"],curpath,signInfo["targetApk"],curpath,signInfo["keystoreAlias"]))
	else:
		return r2

	jarsignerResultLog = '===log===签名结果：%s' % r3
	print(jarsignerResultLog)
	logFile.write(jarsignerResultLog + '\n')

	if r3 != 0:
		return r3

	# 返回签名结果
	return 0


# 判断是否反编译成功
if r == 0:
	jsonStr = open(sys.argv[1])
	signInfos = json.load(jsonStr)
	# 从传入的json文件中读取签名信息
	for signInfo in signInfos:
		signingLog = '\n================正在打包%s.apk================\n' % signInfo["targetApk"]
		print(signingLog)
		logFile.write(signingLog + '\n')

		# 调用签名方法
		signResult = signTask(signInfo)
		print('===log===打包结果：%s' % signResult)
		if signResult == 0:
			signResultLog = '\n================%s.apk================已打包好!\n' % signInfo["targetApk"]
			print(signResultLog)
			logFile.write(signResultLog)
		else:
			signResultLog = '\n================%s.apk================打包失败!!!\n' % signInfo["targetApk"]
			print(signResultLog)
			logFile.write(signResultLog + '\n')
			errorFile.write(signInfo["targetApk"] + '\n')

	# 5, 删除解包文件夹
	shutil.rmtree('%s/unsigned' % curpath)

# 关闭文件
logFile.close()
errorFile.close()
