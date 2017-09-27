import bird_entry
import traceback

def main():
	bdb = bird_entry.BirdEntry("birds.db")
	in_str = "empty"
	while in_str != "":
		in_str = input('Add Table(t) or Entry(e): ')
		if in_str == '':
			continue
		if in_str == 't':
			name_str = input('Table name: ')
			name_val = input('Column Names and Datatype (pair comma separated, tuples | separated): ')
			col_names = name_val.split('|')
			col_tups = list(map(lambda x: (x.split(',')[0], x.split(',')[1]), col_names))
			col_tups = [("BirdId","INT")] + col_tups
			try:
				bdb.create_table(name_str, col_tups)
			except Exception as err:
				print('Table not created: ' + str(err))
				traceback.print_exc()
		if in_str == 'e':
			name_tab = 'empty'
			while name_tab != "":
				name_tab = input("Table name: ")
				if name_tab == '':
					continue
				tab = bdb.find_table(name_tab)
				if type(tab) == type(None):
					print('Table "' + name_tab + '" not found')
					name_tab=""
					continue
				print('                                              ' + str(tab))
				name_val = input("Values (NULL for null data, comma delimited): ")
				vals = name_val.split(',')
				try:
					bdb.add_entry(name_tab, vals)
				except Exception as err:
					print('Entry not added: ' + str(err))
					traceback.print_exc()
					
main()