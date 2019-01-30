#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import types

seps = []

def extract_sep(node, depth):
	t = node['type']

	if t == 'text/x-moz-place-separator':
		seps.append(node)

def pprint(node, depth):
	t = node['type']

	if t == 'text/x-moz-place-separator':
		print('\t' * depth + '---')
	elif t == 'text/x-moz-place':
		print('\t' * depth + node['title'])
	elif t == 'text/x-moz-place-container':
		print('\t' * depth + '+' + node['title'])
	else:
		print('Unkown type %s encountered' % t)

def traverse(node, hook = lambda n, d,: None, depth = 0):

	t = node['type']
	hook(node, depth)
	if t == 'text/x-moz-place-container' and 'children' in node:
		for c in node['children']:
			traverse(c, hook, depth + 1)

if __name__ == '__main__':

	# Read bookmarks file:
	with open("bookmarks.json", "r") as f:
		data = json.load(f)

	traverse(data, pprint)
	traverse(data, extract_sep)
	print(seps)
