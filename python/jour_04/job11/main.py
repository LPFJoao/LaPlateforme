def time_to_text(minutes):

    heures = minutes // 60   

    rest_minutes = minutes % 60  

    print(f"{heures} heures et {rest_minutes} minutes")


time_to_text(int(input("Type here the number of minutes you want to calculate: "))) 