import sqlite3


class Database:
	"""Creating a database"""
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price INTEGER)")
		self.conn.commit()


	def fetch(self):
		self.cur.execute("SELECT * FROM parts")
		rows = self.cur.fetchall()
		return rows

	def insert(self, part,customer,retailer,price):
		self.cur.execute('INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)',(part,customer,retailer,price))
		self.conn.commit()

	def remove(self, id):
		self.cur.execute('DELETE FROM parts WHERE id=?', (id,))
		self.conn.commit()

	def update(self, id,part,customer,retailer,price):
		self.cur.execute('UPDATE parts SET part=?, customer=?,retailer=?,price=?',(part,customer,retailer,price))
		self.conn.commit()


	def __del__(self):
		self.conn.close()

# db = Database('data_store.db')
# db.insert('ram', 'bappa', 'google',	 130)
# db.insert('screen', 'yacks', 'dropbox', 100)
# db.insert('HDD', 'bapps_G', 'microsoft', 121)
# db.insert('pci', 'ymifmah', 'amazon', 110)



