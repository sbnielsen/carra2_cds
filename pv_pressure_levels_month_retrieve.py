import cdsapi

dataset = "reanalysis-pan-carra"
request = {
    "level_type": 'pressure_levels',
    "variable": 'potential_vorticity',
    "pressure_level": [
            '10', '20', '30',
            '50', '70', '100',
            '150', '200', '250',
            '300', '400', '500',
            '600', '700', '750',
            '800', '825', '850',
            '875', '900', '925',
            '950', '1000',
                      ],
    "product_type": 'analysis',
    "time": [
        "00:00", "03:00", "06:00",
        "09:00", "12:00", "15:00",
        "18:00", "21:00"
            ],
    "year": ["2008"],
    "month": ["03"],
    "day": [
            '13', '14', '15',
            '16', '17', '18',
           ],
    "data_format": 'netcdf',
}
 
client = cdsapi.Client()
client.retrieve(dataset, request).download()
