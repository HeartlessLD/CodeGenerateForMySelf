#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
import sys
import datetime
import getpass

def templateReplace(src):
	#print 'template = ' + "'" + src + "'"
	for index, param in enumerate(PARAMS):
		src = src.replace("${param" + str(index) + "}", PARAMS[index])
	#print "generateCode = " + "'" + src + "'"
	src = src.replace("${time}", TIME)
	src = src.replace("${author}", AUTHOR)
	return src
def generateCode(templateName):
	print "begin generate " + templateName
	filePath = CURRENT_PATH + "/" + templateName
	templateFile = open(filePath)
	
	index = templateName.find(".")
	codeFile = open(CURRENT_PATH + "/" + GENERATE_NAME + templateName[index:], "w")
	lines = templateFile.readlines()
	configlLine = lines[0]

	for index,fileLine in enumerate(lines):
		
		fileLine = templateReplace(fileLine)

		
		codeFile.writelines(fileLine)

	templateFile.close()
	codeFile.close()


################main code##################
PARAMS = []
for index, param in enumerate(sys.argv):
	# 第一位是路径 第二位是文件名称 
	if(index <= 1):
		continue
	print sys.argv[index]
	PARAMS.append(sys.argv[index])
if(len(sys.argv) < 2):
	print "Parameters must be determined more than 1 "
	sys.exit(0)
TIME = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
AUTHOR = getpass.getuser()
CURRENT_PATH = os.getcwd()
GENERATE_NAME = sys.argv[1]
current_files = os.listdir(CURRENT_PATH)
for fileName in current_files:
	if(fileName.find("template") != -1):
		generateCode(fileName)
print("generate successful")

