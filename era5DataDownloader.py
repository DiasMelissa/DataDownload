from cdsapi import Client
import pandas as pd

class Era5Downloader:
    _DATA_VARIABLES = [
        'divergence',
        'fraction_of_cloud_cover',
        'geopotential',
        'ozone_mass_mixing_ratio',
        'potential_vorticity',
        'relative_humidity',
        'specific_cloud_ice_water_content',
        'specific_cloud_liquid_water_content',
        'specific_humidity',
        'specific_rain_water_content',
        'specific_snow_water_content',
        'temperature',
        'u_component_of_wind',
        'v_component_of_wind',
        'vertical_velocity',
        'vorticity'
    ]
    
    _DATA_PRESSURE_LEVELS = [
        '1000', '950', '900', '850', '800', '750',
        '700', '650', '600', '550', '500', '450',
        '400', '350', '300', '250', '200', '150', '100'
    ]
    
    _DATA_DOMAIN = [10, -10, -10, 10]
    
    @staticmethod
    def downloadData(initialDate: str, endDate: str) -> None:
        client = Client()
        
        hours = [f'{i:02d}:00' for i in range(24)]
        dates = [date.strftime('%Y-%m-%d') for date in pd.date_range(initialDate, endDate, freq='D')]
        
        requestParameters = {
            'variable': Era5Downloader._DATA_VARIABLES,
            'pressure_level': Era5Downloader._DATA_PRESSURE_LEVELS,
            'product_type': 'reanalysis',
            'format': 'grib',
            'area': Era5Downloader._DATA_DOMAIN,
            'date': dates,
            'time': hours
        }
        
        client.retrieve('reanalysis-era5-single-levels', requestParameters, f'ERA5_{initialDate}_{endDate}.grib')
        
if __name__ == "__main__":
    initialDate = input("Please, enter the start date in the format (YYYY-MM-DD): ")
    endDate = input("Please enter the end date in the format (YYYY-MM-DD): ")

    Era5Downloader.downloadData(initialDate, endDate)