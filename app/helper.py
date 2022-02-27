import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory

#rootdir = os.getcwd()
print(url_for('helper.py'))

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		print(os.path.join(subdir,file))