hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
print((((hour*60+mins+dura)//60)%24) , ":" , ((mins+dura)%60) , sep="")
