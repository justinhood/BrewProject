from Recipe import Recipe
import numpy as np

#Make a test recipe:
tester=Recipe()
tester.setCategory("Cider")
tester.setName("BrewDevil")
tester.setFlavor("Standard Cider, no additional fruit")
tester.setYeast("Brew Devil Brand")
tester.setGoalABV(0)
tester.setOG(0)
tester.setFG(0)
tester.addIngredient("1.5C Granulated White Sugar")
tester.addIngredient("1 Can Brew Devil Cider Concentrate")
tester.addIngredient("2 Gallons Water- Chippewa Valley Spring Water")
tester.setTasteNotes("Pre-Yeast: Not particularly strong flavor, watery and sweet. low acidiy")
tester.setStartDate("2020-10-08")
tester.printRecipe()

tester.writeRecipe()
