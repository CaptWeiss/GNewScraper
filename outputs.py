import os
import json


def output_json(data, name):
	if 'json' not in os.listdir():
		os.mkdir('json')
	data['length'] = len(data["entries"])
	with open(f'json/{name.replace(" ","-").replace("+", "-")}.json', 'w') as f:
		json.dump(data, f, indent=4)

