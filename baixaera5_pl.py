import cdsapi
import pandas as pd

# Variables of interest

vars = ['geopotential', 'relative_humidity', 'specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']

# Domain of interest
#extent = [-100, 10, -50, 10]

# Pressure levels
levels = ['1', '2', '3', '5', '7', '10',
            '20', '30', '50', '70', '100', '125',
            '150', '175', '200', '225', '250', '300',
            '350', '400', '450', '500', '550', '600',
            '650', '700', '750', '775', '800', '825',
            '850', '875', '900', '925', '950', '975',
            '1000']

# Initial date
idate = '2013-12-06'

# Final date
edate = '2013-12-06'

# Data range
dates = [date.strftime('%Y-%m-%d') for date in pd.date_range(idate, edate, freq='D')]

# Time range
hours = [f'{i:02d}:00' for i in range(24)]

# Request parameters for pressure level data
pressure_params = {
    'variable': vars,
    'pressure_level': levels,
    'product_type': 'reanalysis',
    'format': 'grib',
    'date': dates,
    'time': '00:00'
}

print(pressure_params)



c = cdsapi.Client()

c.retrieve('reanalysis-era5-pressure-levels', pressure_params, f'ERA5_{idate}_00-pl.grib')