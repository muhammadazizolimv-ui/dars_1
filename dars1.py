from matplotlib import pyplot as plt

sanalar = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21','22', '23', '24', '25', '26', '27', '28', '29', '30']
sonlar_sentabr = [33, 81, 61, 92, 34, 79, 48, 55, 86, 97, 52, 88, 23, 2, 1, 89, 41, 37, 89, 71, 78, 69, 53, 87, 51, 56, 28, 84, 82, 82]

sonlar_oktabr = [42, 76, 29, 91, 57, 64, 18, 83, 35, 96, 47, 72, 24, 59, 8, 87, 31, 68, 94, 53, 16, 79, 44, 98, 37, 62, 21, 85, 49, 73]
plt.plot(sanalar,sonlar_sentabr,label="sentabr",marker="o",linestyle="dashed")
plt.plot(sanalar,sonlar_oktabr,label="oktabr",color="red",marker="*")

plt.title("Sentabr va oktabr")
plt.xlabel("kunlar")   
plt.ylabel("sotuvlar soni")

plt.legend()   
plt.grid(True) 

#plt.show()
plt.savefig("sotuvlar")