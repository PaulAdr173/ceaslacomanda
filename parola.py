parola = "PaulAdr173"
incercare = str(input("Introduceti parola:"))
count = 0
for x in range(3):
    if(parola == incercare):
        print("Bine ai venit Paul!")
        break
    else:
        print("Mai incearca!")
        incercare = str(input("Introduceti parola:"))
        count += 1
        if(count == 3):
            print("Ne pare rau")
    
