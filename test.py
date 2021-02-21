import matplotlib.pyplot as plt
ori=range(10)
data=[[i,i+2,i+4] for i in ori]
data2=[[i+1,i+3] for i in ori]
print(data)
# plt.scatter(data)

a=plt.figure()
# ax=a.subplot(2,3,1)
# ax.plot(data,label='a')
# ax.legend()
# ax=plt.subplot(2,3,5)
# ax.plot(data,label='a')
# ax.legend()
# ax=plt.subplot(2,3,5)
# ax.plot(data2,label='a')
# ax.legend()

plt.plot(data2)

plt.show()