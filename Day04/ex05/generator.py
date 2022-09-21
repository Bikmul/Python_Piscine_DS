import resource
import sys

def my_reader(filename: str) -> list:
	with open(filename, 'r',) as file:
		tmp_line = 'temp'
		while tmp_line:
			tmp_line = file.readline()
			yield tmp_line


def main(path):
	for line in my_reader(path):
		pass

	memory = resource.getrusage(resource.RUSAGE_SELF)
	print(f'Peak Memory Usage = {(memory.ru_maxrss / (1024**3)):.3f} GB')
	print(f'User Mode Time + System Mode Time = {(memory.ru_utime + memory.ru_stime):.2f}s')


if __name__ == '__main__':
	if (len(sys.argv) == 2):
		main(sys.argv[1])