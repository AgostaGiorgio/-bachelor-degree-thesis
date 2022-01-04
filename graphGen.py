
import matplotlib.pyplot as plt

x = ['50', '25', '10', '5', '2']



y1 = [2.14133, 2.14303, 2.14572, 2.14305, 2.14717]
#y1 = [el*100 for el in y1]
y1.reverse()
plt.plot(x, y1, label="G-WUP base", marker='s', linestyle='dashed')

y2 = [2.13272, 2.13625, 2.14268, 2.13872, 2.14545]
#y2 = [el*100 for el in y2]
y2.reverse()
plt.plot(x, y2, label="G-WUP with Auto-WakeUp", marker='o')



plt.xlabel('Packet inter-arrival time [s]')
plt.ylabel('Number of hops')

plt.legend()

#plt.show()
plt.savefig('foo.png')
