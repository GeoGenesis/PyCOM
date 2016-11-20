
class Weapon():

	def __init__(self,atk,ammo,fr):
		self.atk = atk
		self.full_clip = ammo
		self.ammo = ammo
		self.fire_rate = fr

	def info(self):
		print (self.atk)
		print (self.full_clip)
		print (self.ammo)
		print (self.fire_rate)

	def fire(self,target):
		target.damage(self.atk * self.fire_rate)
		self.ammo = (self.ammo- self.fire_rate)

	def reload(self):
		self.ammo = self.full


class Player():
	
	def __init__(self,alliance,unit):
		
		#Unit Details
		self.unit_alliance = alliance.upper()
		self.unit_type = unit.upper()
		
		#Unit Set Health
		if self.unit_type == "SOLDIER":
			self.health = 10
		elif self.unit_type == "TANK":
			self.health = 75
		elif self.unit_type == "FIGHTER":
			self.health = 60
		else:
			self.health = 0

	def info(self):
		print (self.unit_alliance)
		print (self.unit_type)
		print (self.health)

	def getAlliance(self):
		return self.unit_alliance

	def getType(self):
		return self.unit_type

	def getHealth(self):
		return self.health

	def damage(self,damage):
		self.health = (self.health - damage)

	def IFF(self,target):

		if target.unit_alliance == self.unit_alliance:
			print("TARGET IS FRIENDLY")
		
		elif target.unit_alliance == "NEUTRAL":
			print("TARGET NON-HOSTILE")
		
		elif target.unit_alliance == "HOSTILE":
			print("HOSTILE IDENTIFIED")
		else: 
			print("TARGET UNIDENTIFIED")



w1 = Weapon(5,100,3)
p1 = Player("FRIENDLY", "TANK")
n1 = Player("NEUTRAL", "FIGHTER")
e1 = Player("HOSTILE", "SOLDIER")