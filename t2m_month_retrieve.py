import cdsapi

dataset = "reanalysis-pan-carra-means"
request = {
    "time_aggregation": "monthly",
    "level_type": "single_levels",
    "variable": ["2m_temperature"],
    "product_type": "analysis_based",
    "year": ["1986"],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "data_format": "netcdf"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
