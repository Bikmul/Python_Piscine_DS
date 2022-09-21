import resource
import sys

def my_reader(path):
	df = open(path, 'r')
	lines = df.readlines()
	df.close()
	return lines


def main(path):
	lines = my_reader(path)

	for line in lines:
		pass

	memory = resource.getrusage(resource.RUSAGE_SELF)
	print(f'Peak Memory Usage = {(memory.ru_maxrss / (1024**3)):.3f} GB')
	print(f'User Mode Time + System Mode Time = {(memory.ru_utime + memory.ru_stime):.2f}s')


if __name__ == '__main__':
	if (len(sys.argv) == 2):
		main(sys.argv[1])