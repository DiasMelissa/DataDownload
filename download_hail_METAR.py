# Script of download GR METAR from SBMT #
# ------------------------------------- #
# Created by Melissa Dias #
# ------------------------------------- #
# Required modules
import requests
from datetime import timedelta, date


# Datetime to process and station
station = 'SBMT'
initialData = date(2022, 10, 1)

finalData = date (2023, 3, 31)


# Consult each day and save only the files that have a hail record
delta = timedelta(days=1)

while initialData <= finalData:
    day_str= initialData.strftime('%Y%m%d')
    # Metar data URL 
    url = f'https://www.redemet.aer.mil.br/api/consulta_automatica/index.php?local={station}&msg=metar&data_ini={day_str}00&data_fim={day_str}23&tipo=txt&formato=br'
    # HTTP request
    response = requests.get(url)

    if response.status_code == 200:
        # Filter GR cases
        metar_lines = response.text.split(',')
        metar_hail = [line for line in metar_lines if 'GR' in line]
        
        # Save the result in a TXT file
        if metar_hail:
            with open(f'{day_str}_hail.txt', 'w') as f:
                f.write('\n'.join(metar_hail))
                print(f'File {day_str}_hail.txt was saved with success')
        # Download all the METAR data
        #with open(f'{day_str}_all.txt', 'w') as f:
        #    for line in metar_lines:
        #        f.write(line +'\n')
            
    else:
        print(f'Erro {response.status_code} to do the consult for {day_str}')

    # Next day
    initialData += delta


