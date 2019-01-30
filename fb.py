#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import types

seps = []

def extract_sep(n, i):
	seps.append(n)

def pprint_title(n, i):
	print('\t' * i + n['title'])

def pprint_sep(n, i):
	print('\t' * i + '---')

def traverse(node, hook_place = lambda n, i: None,
	hook_sep = lambda n, i: None, depth = 0):

	t = node['type']

	if t == 'text/x-moz-place-separator':
		hook_sep(node, depth)
	elif t == 'text/x-moz-place':
		hook_place(node, depth)
	elif t == 'text/x-moz-place-container':
		print('\t' * depth + '+' + node['title'])
		if 'children' in node:
			for c in node['children']:
				traverse(c, hook_place, hook_sep, depth + 1)
	else:
		print('Unkown type %s encountered' % d['type'])

if __name__ == '__main__':

	# Read bookmarks file:
	with open("bookmarks.json", "r") as f:
		data = json.load(f)

	traverse(data, pprint_title, pprint_sep)
	        # if isinstance(data, types.DictType):
		# 	print('True!')

	traverse(data, hook_sep = extract_sep)
	print(seps)
