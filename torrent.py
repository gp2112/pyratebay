import requests

URL = "https://apibay.org/"

class Torrent:

	def __init__(self, id, name, info_hash, le, se, num_files, size, username, added, status, category):
		self.id = id
		self.url = 'https://thepiratebay.org/description.php?id='+id
		self.name = name
		self.info_hash = info_hash
		self.leechers = le
		self.seeders = se
		self.num_files = num_files
		self.size = size
		self.username = username
		self.added = added
		self.status = status
		self.category = category
		self.description = None

	def get_description(self):
		if self.description == None:
			r = requests.get(URL+'t.php', params={'id':self.id})
			try:
				tor = r.json()
				self.description = tor['descr']
			except Exception as e:
				print('Error: ', e)

	def magnet(self):
		return f'magnet:?xt=urn:btih:{self.info_hash}&dn={self.name}'

	def __str__(self):
		return f'Name: {self.name}\nHash: {self.info_hash}\nURL: {self.url}'