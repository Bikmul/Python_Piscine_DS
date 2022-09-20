#!/usr/local/bin/python3

def to_dictionary():

	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12')
    ]

	dct ={}

	for i, j in list_of_tuples:
		if j in dct:
			dct[j].append(i)
		else:
			dct[j] = [i]
	
	for key, value in dct.items():
		for item in value:
			print(f"'{key}' : '{item}'")

if __name__=='__main__':
	to_dictionary()
	