import argparse
import os
import sys


def env_to_yaml(env_file='.env', yaml_file='env.yml'):
	"""Creates a .yml file, and populates it with the key/value pairs from 
	`env_file`
	"""
	if not os.path.exists(env_file):
		sys.exit("Error: '{env_file}' not found".format(env_file=env_file))
	with open(yaml_file, 'wb') as f:
		f.write('---\n')
		for line in open(env_file):
			if line.startswith('#'):
				continue
			var = line.strip().split('=')
			if len(var) == 2:
				f.write('{key}: {value}\n'.format(key=var[0], value=var[1]))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Creates a .yml file, and \
		populates it with the key/value pairs from a .env file")

	parser.add_argument('-e', action='store', default='.env', 
		help='The filepath of the source .env file')
	parser.add_argument('-y', action='store', default='env.yml', 
		help='The filepath of the destination .yml file')

	args = vars(parser.parse_args())

	env_to_yaml(env_file=args['e'], yaml_file=args['y'])