import os
import json


def output_json(data, keyword):
	if 'json' not in os.listdir():
		os.mkdir('json')
	with open(f'json/{keyword.replace(" ","-").replace("+", "-")}.json', 'w') as f:
		json.dump(data, f, indent=4)

