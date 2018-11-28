hashToWeatherDict = { 
	 1 : "Overcast" ,
	 2 : "Rainy", 
	 3 : "Sunny"
	}

weatherToHashDict = {
         "Overcast" : 1,
         "Rainy" : 2,
         "Sunny" : 3
        } 

play_dict = {
	True : "Yes",
	False : "No"
	}

weather_data = [3, 1, 2, 3, 3, 1, 2, 2, 3, 2, 3, 1, 1, 2]
play_data = [False, True, True, True, True, True, False, False, True, True, False, True, True,False]

for i in range(len(weather_data)):
	print(f'{hashToWeatherDict[weather_data[i]]:10} ==> {play_dict[play_data[i]]:10}')

FrequencyDict = {
        "Overcast" : {"Yes" : 0, "No" : 0},
        "Rainy" : {"Yes" : 0, "No" : 0},
        "Sunny" :  {"Yes" : 0, "No" : 0},
        "Grand Total" : {"Yes" : 0, "No" : 0},
        }

for i in range(len(weather_data)):
    FrequencyDict[hashToWeatherDict[weather_data[i]]][play_dict[play_data[i]]] += 1
    FrequencyDict["Grand Total"][play_dict[play_data[i]]] += 1

print(str(FrequencyDict))    

def PlayProbability(result):
    total = FrequencyDict["Grand Total"]["Yes"] + FrequencyDict["Grand Total"]["No"]
    return FrequencyDict["Grand Total"][result] / total

def WeatherProbability(event):
    total = FrequencyDict["Grand Total"]["Yes"] + FrequencyDict["Grand Total"]["No"]
    return (FrequencyDict[event]["Yes"] + FrequencyDict[event]["No"]) / total

def AprioriProbability(event, result):
    return FrequencyDict[event][result] / FrequencyDict["Grand Total"][result]

def ApostorioriProbability(result, event):
    return AprioriProbability(event, result) * PlayProbability(result) / WeatherProbability(event) 

print(ApostorioriProbability("Yes", "Sunny"))
print(ApostorioriProbability("No", "Overcast"))

