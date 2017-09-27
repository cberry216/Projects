import sqlite3
from functools import reduce

class Table:
	""" Class to represent a table in a database"""
	
	def __init__(self, cursor, tab_name, col_tups):
		self.__cursor = cursor
		self.__tab_name = tab_name
		self.__col_tups = col_tups
		self._id_counter = 0
		
	def add_table(self):
		""" Adds a table to the database"""
		all_columns = reduce(lambda acc, y: acc + y[0] + " " + y[1] + ", ", self.__col_tups, "")
		all_columns = all_columns[:len(all_columns) - 2]
		self.__cursor.execute('CREATE TABLE IF NOT EXISTS ' + self.__tab_name + '(' + all_columns + ');')
		
	def add_entry(self, values):
		""" Adds an entry to the table given the values"""
		# Creating the columns string
		pre_col_lst = list(map(lambda x: x[0], self.__col_tups))
		col_lst = filter(lambda x: values[pre_col_lst.index(x) - 1] != "NULL", pre_col_lst)
		col_str = reduce(lambda acc, y: acc + y + ', ', col_lst, '')
		col_str = col_str[:len(col_str) - 2]
		# Creating the values string
		pre_val_str = filter(lambda x: x != 'NULL', values)
		val_str = reduce(lambda acc, y: acc + '"' + y + '", ' if self.__col_tups[values.index(y)][1] != int
		                 else acc + y + ', ', pre_val_str, '')
		val_str = val_str[:len(val_str) - 2]
		#print(val_str)
		self.__cursor.execute('INSERT INTO ' + self.__tab_name + '(' + col_str + ') VALUES (' + str(self._id_counter) + ', ' + val_str + ');')
		self._id_counter += 1
		
	def __str__(self):
		""" str method to return a formatted string of the columns"""
		ret_str = ""
		for tup in self.__col_tups[1:]:
			ret_str += str(tup[0]) + '=' + str(tup[1]) + ' | '
		return ret_str
		
	def __eq__(self, other):
		""" Returns true if name of table is equal to the string 'other' """
		return self.__tab_name == other