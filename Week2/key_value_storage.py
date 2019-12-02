import os
import tempfile
import argparse
import json


storage_path = os.path.join(tempfile.gettempdir(), "storage.data")

def clear_tmp_path():
	os.remove(storage_path)


def load_json_data():
	if not os.path.exists(storage_path):
		return {}
	with open(storage_path, 'r') as f:
		raw_data = f.read()
		if(raw_data):
			return json.loads(raw_data)
		return{}

def update_json_data(key, value):
	data = load_json_data()
	if key in data:
		data[key].append(value);
	else:
		data[key] = [value, ];
	with open(storage_path, "w") as f:
		f.write(json.dumps(data))

def find_json_value(key):
		json_map = load_json_data()
		return json_map.get(key)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="it's a small script to load key-value data in json fomat and get it through key")
	parser.add_argument("--key", type=str, help="this parameter is a key of this storage.")
	parser.add_argument("--value", type=str, help="this parameter is a value of this storage.")
	parser.add_argument('--clear', action='store_true', help='Clear')
	args = parser.parse_args()

	if args.clear:
		clear_tmp_path()
	elif args.key and args.value:
		update_json_data(args.key, args.value)
	elif args.key:
		print(", ".join(find_json_value(args.key)))
	else:
		print("unknown command")
