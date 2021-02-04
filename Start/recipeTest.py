from Recipe import Recipe
import numpy as np

#Make a test recipe:
tester=Recipe()
tester.setCategory("Mead")
tester.setName("Maverick")
tester.setFlavor("Tropical: Pineapple Citrus")
tester.setYeast("Fleischmanns Yeast-Dry")
tester.setGoalABV(14)
tester.setOG(1.112)
tester.setFG(1.03)
tester.addIngredient("13g Orange Peel")
tester.addIngredient("150g Pineapple Puree")
tester.addIngredient("1360g Honey: Willow Creek Apiaries Potosi, WI")
tester.addIngredient("1C Black Tea: Lipton")
tester.addIngredient("Water to Fill: Chippewa Valley Spring Water")
tester.setTasteNotes("Pre-Yeast: The nose is all honey, hint of the black tea. The taste is much more tea forward, but still primarily honey. Fairly sweet, would guess that honey is derived from wildflowers.")
tester.setStartDate("2020-10-27")
tester.printRecipe()

tester.writeRecipe()
