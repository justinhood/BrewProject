import numpy as np
import datetime as dt

class Recipe:
	def __init__(self, category="NA", name="NA", flavor="NA", yeast="NA", goalABV=0, startDate=dt.date.today(), OG=0, FG=0, ABV=0, ingredientList=[], tasteNotes=""):
		self.category=category
		self.name=name
		self.flavor=flavor
		self.yeast=yeast
		self.goalABV=0
		self.startDate=startDate
		self.OG=OG
		self.FG=FG
		self.ABV=ABV
		self.ingredientList=ingredientList
		self.tasteNotes=tasteNotes
	
	#Category Functions
	def printCategory(self):
		print(self.category)
	def getCategory(self):
		return self.category
	def setCategory(self, cat):
		self.category=cat
	
	#Name Functions
	def printName(self):
		print(self.name)
	def getName(self):
		return self.name
	def setName(self, n):
		self.name=n

	#Flavor Functions
	def printFlavor(self):
		print(self.flavor)
	def getFlavor(self):
		return self.flavor
	def setFlavor(self, f):
		self.flavor=f

	#Yeast Functions
	def printYeast(self):
		print(self.yeast)
	def getYeast(self):
		return self.yeast
	def setYeast(self, y):
		self.yeast=y

	#ABV Goal Functions
	def printGoalABV(self):
		print(self.goalABV)
	def getGoalABV(self):
		return self.goalABV
	def setGoalABV(self,g):
		self.goalABV=g

	#Start Date Functions
	def printStartDate(self):
		print(self.startDate)
	def getStartDate(self):
		return self.startDate
	def setStartDate(self, d):
		self.startDate=d
	
	#OG Functions
	def printOG(self):
		print(self.OG)
	def getOG(self):
		return self.OG
	def setOG(self, o):
		self.OG=o
		self.calcABV()

	#FG Functions
	def printFG(self):
		print(self.FG)
	def getFG(self):
		return self.FG
	def setFG(self, f):
		self.FG=f
		self.calcABV()

	#ABV Functions
	def printABV(self):
		print(self.ABV)
	def getABV(self):
		return self.ABV
	def calcABV(self):
		self.ABV=round(abs(self.OG-self.FG)*131.25,2)
	
	#Ingredient List Functions
	def printIngredientList(self):
		for i in self.ingredientList:
			print(i)
	def getIngredientList(self):
		return self.ingredientList
	def addIngredient(self,i):
		self.ingredientList.append(i)

	#Taste Notes Functions
	def printTasteNotes(self):
		print(self.tasteNotes)
	def getTasteNotes(self):
		return self.tasteNotes
	def setTasteNotes(self, n):
		self.tasteNotes=n

	#Writing to File Functions
	def writeRecipe(self):
		s=self.name+".txt"
		f=open(s,"w")
		f.write(self.category)
		f.write("\n")
		f.write(self.name)
		f.write("\n")
		f.write(self.flavor)
		f.write("\n")
		f.write(self.yeast)
		f.write("\n")
		f.write(str(self.goalABV))
		f.write("\n")
		f.write(self.startDate)
		f.write("\n")
		f.write(str(self.OG))
		f.write("\n")
		f.write(str(self.FG))
		f.write("\n")
		f.write(str(self.ABV))
		f.write("\n")
		for i in self.ingredientList:
			f.write(i)
			f.write("\n")
		f.write("iend")
		f.write("\n")
		f.write(self.tasteNotes)
		f.close()

	#Full Print
	def printRecipe(self):
		f=[self.category,self.name,self.flavor,self.yeast,self.goalABV,self.startDate,self.OG,self.FG,self.ABV,self.ingredientList,self.tasteNotes]
		for i in f:
			if(i==self.ingredientList):
				for l in i:
					print(l)
			else:
				print(i)
	
	#Load From File
	def load(self, fname):
		f=open(fname,"r")
		self.category=f.readline()[:-1]
		self.name=f.readline()[:-1]
		self.flavor=f.readline()[:-1]
		self.yeast=f.readline()[:-1]
		self.goalABV=float(f.readline())
		self.startDate=f.readline()[:-1]
		self.OG=float(f.readline())
		self.FG=float(f.readline())
		self.ABV=float(f.readline())
		t=f.readline()[:-1]
		while(t!="iend"):
			self.addIngredient(t)
			t=f.readline()[:-1]
		self.tasteNotes=f.readline()
		f.close()
