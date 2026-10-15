from matplotlib import pyplot as plt

# 2000-2005 yillar uchun O'zbekiston aholisi (million)
yillar = ['2000', '2001', '2002', '2003', '2004', '2005']
aholi = [20.7, 21.1, 21.6, 22.1, 22.6, 23.1]

plt.bar(yillar, aholi,width=0.5, color='red')
plt.title("O'zbekiston aholisining 2000-2005 yillardagi o'sishi")
plt.xlabel("Yillar")
plt.ylabel("Aholi (million kishi)")
plt.grid(True, axis='y')
plt.savefig('ozbekiston_aholisi_2000_2005.png')
plt.close()
plt.title("ozbekisdon aholisi ozsi  bormoqda buncha aholga domlar kerak")
