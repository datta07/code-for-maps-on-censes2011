import sqlite3
#"dist","state","area","pop","lit","Hindu","Muslims","Christian","Sikh","Buddhist","Jain"	
def get_db():
	con = sqlite3.connect("realData.db")
	data=con.execute("select * from data")
	arr=[]
	for i in data:
		arr.append(i)
	con.close()
	return arr

data=get_db()
arr=[]
for i in data:
	per=(int(i[6])/int(i[3]))*100
	if ((per>20)&(per<30)):
		arr.append(i[0])
print(arr)