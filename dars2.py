from matplotlib import pyplot 

kunlar =["chorshanba", "payshanba", "juma", "shanba", "yakshanba", "dushanba", "seshanba"]
harorat = [20, 22, 19, 21, 23, 18, 20]

pyplot.bar(kunlar, harorat, width=0.5, color='orange')
pyplot.title("Haftalik harorat")
pyplot.grid(True)
pyplot.show()