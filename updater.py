import os
import json
from shutil import copy2

def import_json(json_path):
	"""
	json_path: Full path to JSON file (properly escaped string)
	returns JSON object
	"""
	json_file = open(json_path, "r") # Open JSON file
	json_str = json_file.read() # Convert to string
	data = json.loads(json_str) # Convert to JSON object
	json_file.close()
	return data

def import_usb(json_data, root_path, dest):
	"""
	json_data: JSON object
	root_path: Full path to the root folder on the USB (properly escaped string)
	dest: Full path to the database folder on disk (properly escaped string)
	returns updated JSON
	"""
	for path, dirs, files in os.walk(root_path): # Traverses contents of pendrive (DFS) | Assumed folder is titled "root"
		path_separated = path.split("\\") # Each folder in the current shard is indexed in array
		for f in files:
			# print("DEBUG FILENAME --->",f)
			copy2(path + "\\" + f, dest) # Copies to location on disk
			json_data[path_separated[1]][path_separated[2]][path_separated[3]] = json_data[path_separated[1]][path_separated[2]][path_separated[3]] + [f] # Updates JSON 
	return json_data

# Following code commits changes to the JSON
def export_json(json_path, json_data):
	"""
	json_path: Full path to JSON file (properly escaped string)
	json_data: JSON object to be written
	returns nothing
	"""
	json_file = open(json_path, "w+")
	json_file.write(json.dumps(json_data))
	json_file.close()
