import datetime as dt
import tkinter as tk
from Recipe import Recipe

class RecipeDisplay(tk.Tk):
	def __init__(self, recipe):
		tk.Tk.__init__(self)
		#Category Widgets
		self.catLabel=tk.Label(self, text="Category:")
		self.catLabel.grid(row=0, column=0)
		self.catEntry=tk.Entry(self, width=50, justify='center')
		self.catEntry.insert(0,recipe.getCategory())
		self.catEntry.config(state='readonly')
		self.catEntry.grid(row=0, column=1)

		#Name Widgets
		self.nameLabel=tk.Label(self, text="Name:")
		self.nameLabel.grid(row=1, column=0)
		self.nameEntry=tk.Entry(self, width=50, justify='center')
		self.nameEntry.insert(0,recipe.getName())
		self.nameEntry.config(state='readonly')
		self.nameEntry.grid(row=1,column=1)

		#Flavor Widgets
		self.flavorLabel=tk.Label(self, text="Flavor Profile:")
		self.flavorLabel.grid(row=2, column=0)
		self.flavorEntry=tk.Entry(self, width=50, justify='center')
		self.flavorEntry.insert(0,recipe.getFlavor())
		self.flavorEntry.config(state='readonly')
		self.flavorEntry.grid(row=2,column=1)

		#Yeast Widgets
		self.yeastLabel=tk.Label(self, text="Yeast Type:")
		self.yeastLabel.grid(row=3, column=0)
		self.yeastEntry=tk.Entry(self, width=50, justify='center')
		self.yeastEntry.insert(0,recipe.getYeast())
		self.yeastEntry.config(state='readonly')
		self.yeastEntry.grid(row=3,column=1)

		#Date/Age Widgets
		self.dateLabel=tk.Label(self, text="Start Date:")
		self.dateLabel.grid(row=4, column=0)
		self.dateEntry=tk.Entry(self, width=50, justify='center')
		self.dateEntry.insert(0,recipe.getStartDate())
		self.dateEntry.config(state='readonly')
		self.dateEntry.grid(row=4,column=1)
		t=recipe.getStartDate().split("-")
		self.ageLabel=tk.Label(self, text="Age (Days):")
		self.ageLabel.grid(row=4, column=2)
		self.ageEntry=tk.Entry(self, width=15, justify='center')
		self.ageEntry.insert(0,(dt.date.today()-dt.date(int(t[0]),int(t[1]),int(t[2]))).days)
		self.ageEntry.config(state='readonly')
		self.ageEntry.grid(row=4, column=3)

		#OG Widgets
		self.ogLabel=tk.Label(self, text="Original Gravity:")
		self.ogLabel.grid(row=5, column=0)
		self.ogEntry=tk.Entry(self, width=50, justify='center')
		self.ogEntry.insert(0,recipe.getOG())
		self.ogEntry.config(state='readonly')
		self.ogEntry.grid(row=5,column=1)
		#FG Widgets
		self.fgLabel=tk.Label(self, text="Final Gravity:")
		self.fgLabel.grid(row=5, column=2)
		self.fgEntry=tk.Entry(self, width=15, justify='center')
		self.fgEntry.insert(0,recipe.getFG())
		self.fgEntry.config(state='readonly')
		self.fgEntry.grid(row=5,column=3)

		#GoalABV Widgets
		self.goalLabel=tk.Label(self, text="Goal ABV (%):")
		self.goalLabel.grid(row=6, column=0)
		self.goalEntry=tk.Entry(self, width=50, justify='center')
		self.goalEntry.insert(0,recipe.getGoalABV())
		self.goalEntry.config(state='readonly')
		self.goalEntry.grid(row=6,column=1)
		#Actual ABV Widgets
		self.actLabel=tk.Label(self, text="Actual ABV (%):")
		self.actLabel.grid(row=6, column=2)
		self.actEntry=tk.Entry(self, width=15, justify='center')
		self.actEntry.insert(0,recipe.getABV())
		self.actEntry.config(state='readonly')
		self.actEntry.grid(row=6,column=3)

		#Ingredients Widgets
		self.ingLabel=tk.Label(self, text="Ingredients:")
		self.ingLabel.grid(row=7, column=0)
		t=recipe.getIngredientList()
		self.ingEntry=tk.Text(self, width=50, height=len(t)+1)
		for x in t:
			self.ingEntry.insert(tk.END,x+"\n")
		self.ingEntry.config(state='disabled')
		self.ingEntry.grid(row=7, column=1)

		#Note Widgets
		self.noteLabel=tk.Label(self, text="Notes:")
		self.noteLabel.grid(row=8, column=0)
		self.noteEntry=tk.Text(self, width=50, height=5)
		self.noteEntry.insert(0.0, recipe.getTasteNotes())
		self.noteEntry.config(state='disabled')
		self.noteEntry.grid(row=8, column=1)

test=Recipe()
test.load("./Recipes/BrewDevil.txt")
app=RecipeDisplay(test)
app.mainloop()
