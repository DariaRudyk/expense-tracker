from tkinter import *
from pandas import *
from time import sleep


window = Tk()
window.title("tracker")

data = read_excel("statement (6).xlsx")

window.geometry("800x800+220+100")
total = Label(window, text = "blallala", bg = "lightblue")
total.place(x = 150, y = 100,  width = 300, height = 100)

categories = {}
cat_list = sorted(set(data.iloc[:,2]))
#print(cat_list)


for i, category in enumerate(cat_list):
	categories[category] = {"label" : Label(window, text = category + " 0", bg = "lightblue"), "amount" : 0}
	categories[category]["label"].place(x = 550, y = 100 + i * 50,  width = 200, height = 50)


#print(categories)

permissions = dict(zip(cat_list, [[30,70],[20,40], [50, 80], [30,50], [200,400], [50, 70],[30,50], [100,150],[50,100]]))
info = Label(window, text = "")
info.place(x = 150, y = 300)
#print(permissions)
total_number = 0

for i in range(44):
	info.config(text = data.values[i][1])
	total_number += data.values[i][-1]
	total.config(text = "total expenses: \n " +  str(round(total_number, 1)))

	#if total_number > 1500:
		#left.config(bg = "blue")

	for category in cat_list:
		if data.values[i][2] == category:
			categories[category]["amount"] += round(data.values[i][-1])
			categories[category]["label"].config(text = category + " " + str(categories[category]["amount"]))


			if categories[category]["amount"] > permissions[category][0]:
				categories[category]["label"].config(bg = "blue")
			if categories[category]["amount"]  > permissions[category][1]:
				categories[category]["label"].config(bg = "red")
			window.update()
			sleep(0.2)


window.update()
sleep(0.2)


"""

def fill(event = None):
	left.config(text = "kuku")
	total.config(text = "mumu")
	
but = Button(window, text = "push the button", width = 11, command = fill)
but.place(x = 250, y = 200)

window.bind("<space>", fill)



"""







"""


left = Label(window, text = "blallala", bg = "lightblue")
left.place(x = 550, y = 100,  width = 200, height = 50)


grocery_store = Label(window, text = "grocery store", bg = "lightblue")
grocery_store.place(x = 550, y = 150,  width = 200, height = 50)

alcohol_count = 0

categories["alcohol"] = Label(window, text = "alcohol " + str(alcohol_count), bg = "lightblue")
categories["alcohol"].place(x = 550, y = 200,  width = 200, height = 50)

pharmacy = Label(window, text = "pharmacy", bg = "lightblue")
pharmacy.place(x = 550, y = 250,  width = 200, height = 50)

cars_and_gas = Label(window, text = "cars and gas", bg = "lightblue")
cars_and_gas.place(x = 550, y = 300,  width = 200, height = 50)

cafe_and_rest = Label(window, text = "cafe and restaurants", bg = "lightblue")
cafe_and_rest.place(x = 550, y = 350,  width = 200, height = 50)

amazon = Label(window, text = "Amazon", bg = "lightblue")
amazon.place(x = 550, y = 400,  width = 200, height = 50)

transportation = Label(window, text = "transportation", bg = "lightblue")
transportation.place(x = 550, y = 450,  width = 200, height = 50)


"""




























