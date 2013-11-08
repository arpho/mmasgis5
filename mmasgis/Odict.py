class Odict(dict):
	"""
	implementa un' ordered dict estendendo la classe dict
	crea una lista che memorizza le chiavi inserite nel dict  con lo stesso ordine di inserimento
	"""
	def __init__(self):
		self.order=[]
		
	def __setitem__(self, key, value):
		"""
		override di __setitem__
		oltre alle normali operazioni di __setitem__ inserisce le chiavi in self.order,
		 solo se la chiave non e'  gia' presente nell'istanza di odict 
		@param key: come in dict 
		@param value:come in dict
		"""
		#aggiungo le chiavi nell'ordine di inserimento
		if not self.has_key(key):
			self.order.append(key)
		dict.__setitem__(self, key, value)
		
	def pop(self,k):
		"""overload del metodo pop per i dict
		@param Object: chiave da rimuovere
		@return: Object, value legato alla chiave rimossa 
		"""
		v=self[k]		
		for i in self.order:
			if i==k:
				self.order.remove(i)
		self.__delitem__(k)

		return v
		
	def clear(self):
		"""overload del metodo clear per i dict"""
		dict.clear(self)
		self.order=[]
		
	def iterkeys(self):
		"""
		override del metodo iterkeys invece dell'iteratore di dict ritorna la lista delle chiavi presenti nell'istanza di Odict
		@return [Object
		"""
		return self.order
	
	def getElementList(self):
		"""
		ritorna la lista degli elementi in odict con il loro ordine di inserimento
		@return [object]
		"""
		
		l=[]
		for i in self.order:
			l.append(self[i])
		return l 