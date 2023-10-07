#!/usr/bin/env python
#coding:utf-8

import os
import sys

#确定反编译的输出目录，默认是当前apk所属目录
def get_output_folder():
	if not len(os.path.dirname(_source_apk_path)) == 0:
		out_path = os.path.dirname(_source_apk_path) + '/'
	else:
		out_path = os.path.dirname(_source_apk_path)

	return out_path+"decompile/"


#获取要反编译的apk路径
def get_input_apk_path():
	if len(sys.argv) == 1:
		return raw_input('please input the apk\'s path: ')
	else:
		return sys.argv[1]

def process_user_choice():
	
	print '\n======================Operation========================'
	print '\nGet java source code from apk'
	get_resource()
	print 'Extracting resource success'
	print '\nGet resource and smali code from apk'
	#convert_apk_to_jar()
	print 'Convert to jar success'
	print 'Extracting classes from jar...'
	extract_classes_from_jar()
	print 'Extracting classes success'
	print 'Converting classes to java code...'
	convert_classes_to_java()
	print 'Convert classes to java success'
	print '=======================================================\n'

#获取资源文件
def get_resource():
	print '\nGetting resource...\n'
	os.system('java -jar %s/apktool_2.8.1.jar d -f -o %s %s' % (_running_path, _apk_resource_folder, _source_apk_path))

#将apk转化为jar
def convert_apk_to_jar():
	print 'Converting apk to jar...'
	os.system('sh %s/dex-tools/d2j-dex2jar.sh -f -o %s %s' % (_running_path, _apk_jar, _source_apk_path))

#将class文件从jar包中解压出来
def extract_classes_from_jar():
	if not os.path.exists(_apk_classes_folder):
		print 'Create dir: %s' % _apk_classes_folder
		os.system('mkdir %s' % _apk_classes_folder)
	os.system('unzip -q -o %s -d %s' % (_apk_jar, _apk_classes_folder))

#将classes文件转换为java代码
def convert_classes_to_java():
	if not os.path.exists(_apk_source_code_folder):
		print 'Create dir: %s' % _apk_source_code_folder
		os.system('mkdir %s' % _apk_source_code_folder)
	os.system('find %s -name \"*.class\" | xargs %s/jad -ff -r -nonlb -s java -space -d %s >/dev/null 2>&1' % (_apk_classes_folder, _running_path,_apk_source_code_folder))

#获取此脚本所在的路径
_running_path = os.path.split(os.path.realpath(sys.argv[0]))[0]

#初始化相关变量
_source_apk_path = get_input_apk_path()
_apk_basename = os.path.basename(_source_apk_path).strip()
_apk_basename_without_ext = os.path.splitext(_apk_basename)[0]
_output_folder = get_output_folder()

_apk_resource = 'apk'
_apk_jar = '%s-dex2jar.jar' % (_output_folder + _apk_resource)
_apk_classes_folder = '%s_classes' % (_output_folder + _apk_resource)
_apk_source_code_folder = '%s_source_code' % (_output_folder + _apk_resource)
_apk_resource_folder = '%s_resource' % (_output_folder + _apk_resource)

# print _source_apk_path
# print _output_folder
# print _apk_basename
# print _apk_jar
# print _apk_classes_folder
# print _apk_resource_folder

process_user_choice()




