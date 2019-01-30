#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

seps = []
uris = []
guids = []

def extract_guid(node, depth):
	guids.append(node['guid'])

def extract_sep(node, depth):
	if node['type'] == 'text/x-moz-place-separator':
		seps.append(node)

def extract_uri(node, depth):
	if node['type'] == 'text/x-moz-place':
		uris.append(node['uri'])

def pprint(node, depth):
	t = node['type']

	if t == 'text/x-moz-place-separator':
		print('\t' * depth + str(node['index']) + '---')
	elif t == 'text/x-moz-place':
		print('\t' * depth + str(node['index']) + ': ' + node['title'] + ': ' + node['uri'])
	elif t == 'text/x-moz-place-container':
		print('\t' * depth + '+' + str(node['index']) + node['title'])
	else:
		print('Unkown type %s encountered' % t)

def traverse(node, hook = lambda n, d,: None, depth = 0):
	hook(node, depth)
	if node['type'] == 'text/x-moz-place-container' and 'children' in node:
		for c in node['children']:
			traverse(c, hook, depth + 1)

if __name__ == '__main__':

	# Read bookmarks file:
	with open("bookmarks.json", "r") as f:
		data = json.load(f)

	traverse(data, pprint)
	traverse(data, extract_guid)

	seen = set()
	uguids = []
	for i in guids:
		if i not in seen:
			uguids.append(i)
			seen.add(i)
		else:
			print('Duplicate guid: %s found!' % i)
	print(uguids)
