import click
import csv
from prettytable import PrettyTable
#from operator import itemgetter 

@click.command()
@click.option('--search', prompt='Search for', help='String used for search within given address book file.')
@click.option('--file', default='assets/example.txt', help='Path to the file of the address book.')

def test(search, file):
	#Status
	click.echo('Searching for \"%s\"...' % search)
	contacts = []
	#opens file as csv and compairs search team to each row
	#places matching rows into contacts
	with open(file, 'rb') as inputfile:
		#progress bar
		with click.progressbar( csv.reader(inputfile) ) as bar:
			for row in bar:
				#click.echo(row);
				str1 = ''.join(row)
				str1 = str1.decode('utf-8').strip().lower()
				search = search.decode('utf-8').strip().lower()
				if search in str1:
					contacts.append(row)
					#click.echo(str1);
	#print all matching contacts
	labels = ['First name', 'Last name', 'Street', 'City', 'State', 'Age']
	if contacts:
		t = PrettyTable(labels)
		#sort contacts by last name
		# sorted(contacts, key=itemgetter(1))
		for person in contacts:
			#Clean strings / strips quotes
			person[0] = ''.join(e for e in person[0] if e.isalnum()).title();	#first
			person[1] = ''.join(e for e in person[1] if e.isalnum()).title();	#last
			#person[2] = person[2].title();			#street doesnt work w/ title bc of 2nd/3rd
			person[3] = person[3].title();			#city
			person[4] = person[4].upper();			#state
			t.add_row(person)
		click.echo(t)
	else : 
		click.echo('Sorry, there is no entry matching \"%s\"' % search)

if __name__ == '__main__':
	test()