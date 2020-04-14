from covid import Covid
import tkinter
import time

covid = Covid()

countryList = list()

def ReadFile():
	f = open("countries.txt","r+",encoding = 'utf-8')
	line =f.readline()
	while line:
		countryList.append(line.replace('\n',''))
		line = f.readline()

def QuitApplication():
	quit()

def AddCountries():
	top2 = tkinter.Tk()

	def addCountry():
		f = open("countries.txt","a+",encoding = 'utf-8')
		countryName = nameInp.get()
		if len(countryName)> 0:
			f.write('\n'+countryName)
			print(countryName)

			nameInp.delete(0,tkinter.END)
			top2.destroy()

	top2.geometry('300x300')
	top2.title("Covid Notifier")
	# Labels
	name = tkinter.Label(top2,text="Enter the country name to notify about:")
	name.place(x=10,y=10,width=280,height=25)

	# Inputs
	nameInp = tkinter.Entry(top2)
	nameInp.place(x=10,y=50,width=280,height=25)

	addBtn = tkinter.Button(top2,text="Add Country",command=addCountry)
	addBtn.place(x=100,y=80,width=75,height=25)

	listTxt = tkinter.Label(top2,text = "Countries Watched:\n"+',  '.join(countryList))
	listTxt.place(x=10,y=140,width=280,height=100)

	top2.mainloop()


def GetCovidStats():
	top = tkinter.Tk()
	
	top.geometry('500x500')
	top.title("Covid Notifier")

	listTxt = tkinter.Label(top,text = "Countries Watched:")
	listTxt.place(x=0,y=10,width=250,height=20)

	listTxt = tkinter.Button(top,text = "Add Countries Here", command=AddCountries)
	listTxt.place(x=250,y=10,width=250,height=20)

	headingrow = tkinter.Label(top,text = "Name of country\t | Confirmed Cases\t | Total Deaths\t | Recovered Cases")
	headingrow.place(x=0,y=30,width=500,height=20)

	countryStats=""
	for country in countryList:
		stat = covid.get_status_by_country_name(country)
		name = stat['country']
		confirmed = stat['confirmed']
		deaths = stat['deaths']
		recovered = stat['recovered']
		countryStats+= name.upper()+'\t\t\t'+str(confirmed)+'\t\t'+str(deaths)+'\t\t'+ str(recovered)+'\n'

	countries = tkinter.Label(top,text = countryStats,anchor=tkinter.N)
	countries.place(x=0,y=50,width=500,height=400)

	stop = tkinter.Button(top,text="Stop Permanently",command= QuitApplication)
	stop.place(x=0,y=460,width=500,height=40)


	top.mainloop()


if __name__ == '__main__':
	while(True):
		ReadFile()
		GetCovidStats()
		time.sleep(7200)
		countryList.clear()
