import matplotlib.pyplot as plt
import pandas
import numpy as np

# time=[1,2,3,4,5,6,7]
# speed=[12,14,89,43,56,32,54]
#
#
# plt.plot(time, speed)
# plt.xlabel('time -->')
# plt.ylabel('speed -->')
# plt.show()


data = pandas.read_csv('resources/time_speed.csv', index_col=0)
print(data.head())
plot = data.plot(title="Time Vs Speed 2", lw=2, colormap='jet', marker='.', markersize=5)
plot.set_xlabel('time -->')
plot.set_ylabel('speed -->')
plt.legend
plt.show()