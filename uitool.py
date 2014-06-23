#!/usr/bin/python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# uitool-console: command line uitool tool manager for cocos2d
#
# Author: luowei
# Email: njutcmwl@gmail.com
# ----------------------------------------------------------------------------

import sys
import os

BasePSDDir = 'D:\\kof\\art\\'

#目标PSD
targetFile = ''
#psd文件所在目录
rootpath = ''
#
basename = ''
#psd碎图所在目录
targetDir = ''


def generate():
	#切图
	cutPSD(targetFile)
	#拼接
	plist = os.path.join(rootpath,basename + '/' + basename.capitalize() + '.plist')
	png = os.path.join(rootpath,basename + '/' + basename.capitalize() + '.png')
	generateSheet(targetDir,plist,png)

def cutPSD(filepath):
	sysCmd = ''
	sysCmd = 'uitool %s' % filepath
	print(sysCmd)
	os.system(sysCmd)

def generateSheet(dir,plist,png):
	source = ''
	list = os.listdir(dir)
	#todo 公共资源不打包
	for line in list:
		source += os.path.join(dir,line)
		source += ' '
	sysCmd = ''
	sysCmd = 'Texturepacker  --size-constraints NPOT --format cocos2d --data %s --sheet %s %s ' % (plist, png,source)
	print(sysCmd)
	os.system(sysCmd)

def rmTrees(topPath):
	for root,dirs,files in os.walk(topPath,topdown=False):
		for name in files:
			os.remove(os.path.join(root,name))
		for name in dirs:
			os.rmdirs(os.path.join(root,name))



if __name__ == "__main__":
	print(sys.path)
	print(sys.argv)
	if len(sys.argv) >1 and sys.argv[1]:
		targetFile = sys.argv[1]
	else:
		targetFile = raw_input('please input the path:')	

	if not os.path.exists(targetFile):
		targetFile = BasePSDDir + targetFile + '.psd'
		
	if not os.path.exists(targetFile):
		print(targetFile + ' not exits')
		exit(1)

	rootpath = os.path.dirname(targetFile)
	#转成大写
	basename = os.path.basename(targetFile).capitalize()
	targetFile = os.path.join(rootpath,basename)

	basename = os.path.basename(targetFile).replace('.psd','')
	targetDir = os.path.join(rootpath,basename + '/' + basename)
	print('rootpath=' + rootpath)
	print('targetDir=' + targetDir)

	rmTrees(targetDir)
	generate()
	os.system('start ' + os.path.join(rootpath,basename) )