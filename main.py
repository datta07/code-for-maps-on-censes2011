import sqlite3
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import requests
from difflib import SequenceMatcher
import matplotlib


def getAltName(arr):
	maindata=[]
	con = sqlite3.connect('dummy.db')
	for i in arr:
		data = con.execute('select altNames from altNames where name=?',(i,))
		name = False
		for i in data:
			name = i[0]
		maindata.append(name)
	con.commit()
	con.close()
	return maindata

arr = ['Aurangabad', 'Mumbai City', 'North Twenty Four Parganas', 'Barddhaman', 'Nadia', 'Haora', 'Kolkata', 'Koch Bihar', 'Dakshin Dinajpur', 'Dakshina Kannada', 'Dharwad', 'Kachchh', 'Bharuch', 'Jaisalmer', 'Ghaziabad', 'Lucknow', 'Kheri', 'Budaun', 'Bulandshahar', 'Barabanki', 'Siddharth Nagar', 'Pilibhit', 'Sant Kabir Nagar', 'Baghpat', 'Darbhanga', 'Pashchim Champaran', 'Sitamarhi', 'Palakkad', 'Kannur', 'Wayanad', 'Bhopal', 'Burhanpur', 'Giridih', 'Deoghar', 'Godda', 'Jamtara', 'Lohardaga', 'Kokrajhar', 'Chirang', 'Udham Singh Nagar', 'Palwal', 'Thoubal']
arr = getAltName(arr)

fig, ax = plt.subplots()
map=Basemap(projection="mill",lat_0=54.5, lon_0=-4.36,llcrnrlon=67.8, llcrnrlat=5.5, urcrnrlon=97.4, urcrnrlat=37.5)
map.readshapefile('data/IND_adm2','INDIA')
plt.title('Negligible Muslim population')
for info,shape in zip(map.INDIA_info, map.INDIA):
	if (info['NAME_2'] not in arr):
		ax.add_collection(PatchCollection([Polygon(np.array(shape))], facecolor= '#ffffff' , edgecolor='k', linewidths=.2, zorder=2))
	else:
		ax.add_collection(PatchCollection([Polygon(np.array(shape))], facecolor= (0,1,0,1) , edgecolor='k', linewidths=.2, zorder=2))

plt.show()