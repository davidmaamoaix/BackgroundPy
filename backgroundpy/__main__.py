''' Yep, this is all there is to the package. '''

import os
import sys

def main():
	''' Simple. '''

	''' Initializing arguments. '''
	name = sys.argv[1]
	file = sys.argv[2]

	''' Do da thing. '''
	os.system(f'mkdir {name}')
	with open(os.path.join(os.getcwd(), f'{name}/{name}.sh'), 'w+') as f:
		f.write(
			f'''#!/bin/bash\n'''
			f'''cd "$(dirname "$0")"\n'''
			f'''nohup python .{name}.py & > {name}/{name}.sh'''
			)

main()