import cdsapi

dataset = "reanalysis-pan-carra"
request = {
    "level_type": "height_levels",
    "level_location": [
        "15",
        "30",
        "50",
        "75",
        "100",
        "150",
        "200",
        "250",
        "300",
        "400",
        "500"
    ],
    "variable": [
        "wind_direction",
        "wind_speed"
    ],
    "product_type": "forecast",
    "time": [
        "00:00", "03:00", "06:00",
        "09:00", "12:00", "15:00",
        "18:00", "21:00"
    ],
    "leadtime_hour": [
        "1",
        "2",
        "3"
    ],
    "year": ["2008"],
    "month": ["03"],
    "day": ["03", "04"],
    "data_format": "netcdf",
    "area": [84, -142, 41, -52]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
