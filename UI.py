from covid import Covid
import tkinter

covid = Covid()

countryList = list()
countryStats = list()

def addCountry():
	f = open("countries.txt","a+",encoding = 'utf-8')
	countryName = nameInp.get()
	if not len(countryName):
		f.write('\n'+countryName)
		nameInp.delete(0,tkinter.END)

def readFile():
	f = open("countries.txt","r+",encoding = 'utf-8')
	line =f.readline()
	while line:
		countryList.append(line.replace('\n',''))
		line = f.readline()

def GetCovidStats():
	for country in countryList:
		stat =covid.get_status_by_country_name(country)
		print(stat['country'],stat['confirmed'],stat['deaths'], stat['recovered'])
		countryStats.append(stat)

readFile()
GetCovidStats()
top = tkinter.Tk()
top.geometry('300x300')
top.title("Covid Notifier")
# Labels
name = tkinter.Label(top,text="Enter the country name to notify about:")
name.place(x=10,y=10,width=280,height=25)

# Inputs
nameInp = tkinter.Entry(top)
nameInp.place(x=10,y=50,width=280,height=25)

addBtn = tkinter.Button(top,text="Add Country",command=addCountry)
addBtn.place(x=100,y=80,width=75,height=25)

listTxt = tkinter.Label(top,text = "Countries Watched:\n"+',  '.join(countryList))
listTxt.place(x=10,y=140,width=280,height=100)

top.mainloop()






