#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
No rights reserved. All files in this repository are released into the public
domain.
"""

from setuptools import setup

setup(
	# Some general metadata. By convention, a plugin is named:
	# opensesame-plugin-[plugin name]
	name='opensesame-plugin-Pulse_EVT2',
	version='0.0.1',
	description='Send markers through an EVT2 (RUG USB interface)',
	author='Mark Span',
	author_email='m.m.span@rug.nl',
	url='https://github.com/your/repository',
	# Classifiers used by PyPi if you upload the plugin there
	classifiers=[
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Environment :: Win32 (MS Windows)',
		'License :: OSI Approved :: GNU Public Licence v3',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
	# The important bit that specifies how the plugin files should be installed,
	# so that they are found by OpenSesame. This is a bit different from normal
	# Python modules, because an OpenSesame plugin is not a (normal) Python
	# module.
	data_files=[
		# First the target folder.
		('share/opensesame_plugins/Pulse_EVT2',
		# Then a list of files that are copied into the target folder. Make sure
		# that these files are also included by MANIFEST.in!
		[
			'opensesame_plugins/Pulse_EVT2/Pulse_EVT2.md',
			'opensesame_plugins/Pulse_EVT2/Pulse_EVT2.png',
			'opensesame_plugins/Pulse_EVT2/Pulse_EVT2_large.png',
			'opensesame_plugins/Pulse_EVT2/Pulse_EVT2.py',
			'opensesame_plugins/Pulse_EVT2/libevt.py',
			'opensesame_plugins/Pulse_EVT2/EventExchanger.dll',
			'opensesame_plugins/Pulse_EVT2/HidSharp.dll',
			'opensesame_plugins/Pulse_EVT2/HidSharp.DeviceHelpers.dll',
			'opensesame_plugins/Pulse_EVT2/info.yaml',
			'opensesame_plugins/Pulse_EVT2/Example.osexp',
			]
		)]
	)