_parsed_rows = []

def parse_csv():
    import csv
    _file_path = "./nyc_weather.csv"

    global _parsed_rows
    with open(_file_path, "r") as f:
        reader = csv.reader(f, delimiter=',')
        reader.next()
        for row in reader:
            _parsed_rows.append({
                'date':  row[0],
                'temperature': row[1],
                'DewPoint': row[2],
                'Humidity': row[3],
                'Sea_Level_PressureIn': row[4],
                'VisibilityMiles': row[5],
                'WindSpeedMPH': row[6],
                'PrecipitationIn': row[7],
                'CloudCover': row[8],
                'Events': row[9],
                'WindDirDegrees': row[10]
            })
            
def get_max_temperature():
    max_temp = 0
    for row in _parsed_rows:
        if int(row['temperature']) > max_temp:
            max_temp = int(row['temperature'])
    return max_temp

def get_days_of_rain(event):
    days = []
    for row in _parsed_rows:
        if row['Events'] == event:
            days.append(row['date'])
    return days

def get_avg_wind_speed():
    total = 0
    count = 0
    for row in _parsed_rows:
        speed = 0 if row['WindSpeedMPH']=='' else int(row['WindSpeedMPH'])
        total += speed
        count += 1
    return float(total/count)

if __name__ == '__main__':
    parse_csv()
    
    print ("Max Temperature is : " + str(get_max_temperature()))
    print ("Days of rain : " + str(get_days_of_rain('Rain')))
    print ("Average wind speed is : " + str(get_avg_wind_speed()))

