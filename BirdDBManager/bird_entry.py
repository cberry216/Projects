import sqlite3
import table as tdb
from functools import reduce

class BirdEntry:
	""" Class to add and modify birde entries in bird database"""

	def __init__(self, db_name):
		""" Connects to database and creates a cursor"""
		self.__db = sqlite3.connect(db_name)
		self.__cursor = self.__db.cursor()
		self._tables = []
		tfile = open('table_log.txt', 'w+')
		try:
			while True:
				line = next(tfile).split(';')
				col_tups = line[1]
				col_tups = col_tups.split('|')
				col_tups = tuple(map(lambda x: (x.split(',')[0],x.split(',')[1]), col_tups))
				new_tab = tdb.Table(self.__cursor, line[0], col_tups)
				len_tab = len((self.__cursor.execute("SELECT * FROM " + line[0])).fetchall())
				new_tab._id_counter = len_tab
				self._tables.append(new_tab)
		except StopIteration:
			print("All tables read")
		self._tables_file = open('table_log.txt', 'w')

	def create_table(self, tab_name, col_tups):
		""" Adds a table to the database with table name tab_name and columns named for each value
			in col_tups; col_tups is a list of tuples with the first value being the name and the
			second being the datatype"""
		table = tdb.Table(self.__cursor,tab_name,col_tups)
		table.add_table()
		self.__db.commit()
		self._tables.append(table)
		col_tup_formatted = reduce(lambda acc, y: acc + str(y[0]) + ',' + str(y[1]) + '|', col_tups, '')
		self._tables_file.write(tab_name + ';' + col_tup_formatted)
		
	def add_entry(self, tab_name, values):
		""" Adds a entry to a table with the given values"""
		table = list(filter(lambda x: x == tab_name, self._tables))[0]
		table.add_entry(values)
		self.__db.commit()
		
	def find_table(self, tab_name):
		""" Looks through the table and returns the table that matches the name"""
		for t in self._tables:
			if t == tab_name:
				return t
		return None
		
#be = BirdEntry("birds.db")
#be.create_table("test",[("abc","text"),("def", "text"),("hij","text")])
#be.add_entry('test',['bird_a','bluebird','it is blue'])
#be.add_entry('test',['bird_b','NULL','it is green'])
