import cdsapi

dataset = "reanalysis-pan-carra"
request = {
    "level_type": 'single_levels',
    "variable": ['time_integral_of_rain_flux', 'total_precipitation'],
    "product_type": 'forecast',
    "time": [
            '00:00', '12:00',
            ],
    "leadtime_hour": [
            '6', '9', '12',
            '15', '18',
                     ],
     "year": ['2017'],
     "month": ['09'],
     "day": ['14', '15',],
     "data_format": 'grib',
}
 
client = cdsapi.Client()
client.retrieve(dataset, request).download()
