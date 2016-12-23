from time import sleep
import pickle

class Ayuda:
	
	def __init__(self):
		self.match_pista2 = False
		self.match_pista3 = False
		self.match_pista4 = False
		self.match_pista5 = False
		self.match_pista6 = False
		self.match_clave = False

	def __decodificar__(self, texto):
		tmp = str()
		lista = texto.split()
		for c in lista:
			tmp += chr(int(c, 2))
		return tmp

	def extraer_pista2(self):
		with open("Pista2.ayudantes", "rb") as file:
			tmp = pickle.load(file)
		pista = self.__decodificar__(tmp)
		return pista

	def extraer_pista3(self):
		with open("Pista3.ayudantes", "rb") as file:
			tmp = pickle.load(file)
		pista = self.__decodificar__(tmp)
		return pista

	def extraer_pista4(self):
		with open("Pista4.ayudantes", "rb") as file:
			tmp = pickle.load(file)
		pista = self.__decodificar__(tmp)
		return pista

	def extraer_pista5(self):
		with open("Pista5.ayudantes", "rb") as file:
			tmp = pickle.load(file)
		pista = self.__decodificar__(tmp)
		return pista
	
	def extraer_pista6(self):
		with open("Pista6.ayudantes", "rb") as file:
			tmp = pickle.load(file)
		pista = self.__decodificar__(tmp)
		return pista
		
	def extraer_clave(self):
		with open("Clave.ayudantes", "rb") as file:
			tmp = pickle.load(file)
		clave = self.__decodificar__(tmp)
		return clave

	def comprobar_pista2(self, string_alumno):
		flag1 = False
		flag2 = False
		flag3 = False
		stract1 = "01110101 01101110 01100100 01100001 00100000"
		stract2 = "01101101 01101001 01110100 01100001 01100100"
		stract3 = "01101101 01100101 01101110 01110011 01100001 01101010 01100101"
		if self.__decodificar__(stract1) in string_alumno:
			flag1 = True
			if self.__decodificar__(stract2) in string_alumno:
				flag2 = True
				if self.__decodificar__(stract3) in string_alumno:
					if string_alumno[26] == self.__decodificar__("01101010"):
						flag3 = True
		if flag1==flag2==flag3==True:
			print("Genial!! Acertaste con la segunda pista!")
			self.match_pista2 = True
			return True
		if not flag1:
			print("Uuuuh, aun falta para poder acertar")
		elif not flag2:
			print("Casi...")
		elif not falg3:
			print("Demasiado cerca!")
		return False

	def comprobar_pista3(self, string_alumno):
		if self.match_pista2:
			flag1 = False
			flag2 = False
			flag3 = False
			stract1 = '01110010 01110100 01101001 01100101 01110010'
			stract2 = '01100001 01110011 00100000 01110110 01101111 01100011 01100001 01101100'
			stract3 = '01101110 01100101 00100000 01100100 01100101 01110011'
			if self.__decodificar__(stract1) in string_alumno:
				flag1 = True
				if self.__decodificar__(stract2) in string_alumno:
					flag2 = True
					if self.__decodificar__(stract3) in string_alumno:
						flag3 = True
			if flag1==flag2==flag3==True:
				print('Bien! Cuidado que ahora ya empieza el desafio!')
				self.match_pista3 = True
				return True
			else:
				print('Ups!, esa no era la pista que sirve para entender la siguiente')
				return False
		else:
			print('Debes ingresar correctamente la pista anterior para poder intentar resolver esta')
			return False
	
	def comprobar_pista4(self, string_alumno):
		if self.match_pista3:
			falg1 = False
			falg2 = False
			falg3 = False
			stract1 = '01101110 00100000 01100101 01110011 00100000 01101111'
			stract2 = '01100011 01101001 01101110 01100011 01101111'
			stract3 = '''01100100 01101111 01110011 00100000 01110011 01101001
						01100101 01110100 01100101 00100000 01110100 01110010
						01100101 01110011'''
			if self.__decodificar__(stract1) in string_alumno:
				flag1 = True
				if self.__decodificar__(stract2) in string_alumno:
					flag2 = True
					if self.__decodificar__(stract3) in string_alumno:
						flag3 = True
			if flag1==flag2==flag3==True:
				print('Interesante... nuestro Benevolente Genera...\n Sigue asi!')
				self.match_pista4 = True
				return True
			else:
				print('Uuuf...')
				return False
		else:
			print('LA PISTA ANTERIOOOR!!')
			return False

	def comprobar_pista5(self, string_alumno):
		if self.match_pista4:
			falg1 = False
			falg2 = False
			falg3 = False
			stract1 = '''01101101 01100101 01101110 01110100 01101111 00100000
						01110100 01101111 01101101 01100001 01101110 01100100
						01101111'''
			stract2 = '''01100011 01110101 01100101 01101110 01110100 01100001
						00100000 01100001 01101100 00100000 01100001 01100010
						01100101 01100011 01100101 01100100 01100001 01110010
						01101001 01101111'''
			stract3 = '''01101111 01101110 01101111 01101101 01100001 01110100
						01101111 01110000 01100101 01111001 01100001'''
			if self.__decodificar__(stract1) in string_alumno:
				flag1 = True
				if self.__decodificar__(stract3) not in string_alumno:
					flag2 = True
					if self.__decodificar__(stract2) in string_alumno:
						flag3 = True
			if flag1==flag2==flag3==True:
				print('Una pista mas!')
				self.match_pista5 = True
				return True
			else:
				print('El orden anterior era de palabras...')
				return False
		else:
			print('JGAJGAJGAJGAJGA')
			return False

	def comprobar_pista6(self, string_alumno):
		if self.match_pista5:
			falg1 = False
			falg2 = False
			falg3 = False
			stract1 = '''01101001 01111010 01100001 00100000 01101100 01100001'''
			stract2 = '01100011 01101001 01101110 01100011 01101111 '
			stract3 = '''01110100 01100001 01110010 00100000 01101100 01101111
						01110011 00100000 01100101 01101100 01100101 01101101'''
			if self.__decodificar__(stract1) in string_alumno:
				flag1 = True
				if self.__decodificar__(stract3) in string_alumno:
					flag2 = True
					if self.__decodificar__(stract2) in string_alumno:
						flag3 = True
			if flag1==flag2==flag3==True:
				print('Nuestro General estara orgulloso si descubres la clave secreta')
				self.match_pista6 = True
			else:
				print('NEIN! NEIN! NEIN! NEIN!')
				return False
		else:
			print('Recuerda la pista anterior')
			return False

	def comprobar_clave(self, string_alumno):
		if self.match_pista6:
			flag1 = False
			flag2 = False
			flag3 = False
			stract1 = '''01101001 01101110 01110110 01100101 01110011 01110100
						01101001 01100111 01100001 01100011 01101001 01101111
						01101110 01100101 01110011'''
			stract2 = '01100100 01100001 01110011 00100000 01100100 01100101'
			stract3 = '01100011 01110010 01101001 01100001 01110100 01110101 01110010 01100001 01110011'
			stract4 = '01100001 01110100 01100001 01101110 01100111 01100001 01101110 01100001'
			if self.__decodificar__(stract1) in string_alumno:
				flag1 = True
				if self.__decodificar__(stract4) not in string_alumno:
					if self.__decodificar__(stract2) in string_alumno:
						flag2 = True
						if self.__decodificar__(stract3) in string_alumno:
							flag3 = True
			if  flag1==flag2==flag3==True:
				print('*Sonidos extranios*')
				sleep(1)
				print('-Persona1: Genial! Nuestro Gener...')
				sleep(1)
				print('-????: ALFIN! INCRRREIBLE! TE ESTABAMOS ESPERRRANDO')
				sleep(2)
				print('-Persona1: GENERAL KROLL!!')
				sleep(2)
				print('-Kroll: Esta perrsonita rrresolvio la Tarrrea?')
				sleep(2)
				print('-Persona1: Al parecer s...')
				sleep(0.5)
				print('-Kroll: BIEN! PORRR FIN!')
				sleep(2)
				print('-Perona1: Entonces General, que hacem...')
				sleep(0.5)
				print('-Kroll: HEY TU! BIENIDO AL EJERRCITO DEL BENEVOLENTE GENERRAL KRRROLL')
				sleep(1)
				print('.')
				sleep(1)
				print('.')
				sleep(1)
				print('.')
				sleep(1)
				print('Despues de esto, quizas nunca mas veamos al general Kroll')
				sleep(2)
				print('A no ser que...')
				sleep(3)
				print('Continuara! Felicidades por resolver la tarea!')
				return True
			else:
				print('Acceso denegado!')
				return False
		else:
			print('No se pueden confirmar las otras pistas...')
			return False


