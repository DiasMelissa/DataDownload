import cdsapi
import pandas as pd

# Variables of interest

vars = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio', 
        'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 
        'specific_humidity', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 
        'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity','vorticity']

# Domain of interest
#extent = [-100, 10, -50, 10]

# Pressure levels
levels = ['1000', '950', '900', '850', '800', '750' , 
          '700', '650', '600', '550', '500', '450',
          '400', '350', '300', '250', '200', '150',
          '100']

# Initial date
idate = '2013-12-05'

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
    'time': hours
}

print(pressure_params)



c = cdsapi.Client()

c.retrieve('reanalysis-era5-pressure-levels', pressure_params, f'pres_{idate}_{edate}.grib')