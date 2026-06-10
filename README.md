![logo](./LogoLine_EC_Cop_ECMWF.png)

# CARRA2 CDS Notebooks

This repository contains demonstration Jupyter Notebooks for retrieving, analyzing, and plotting Copernicus Pan-Arctic Regional Reanalysis (CARRA2) data using the Copernicus Climate Data Store (CDS) API.

## Prerequisites

To download data, you will need a CDS API key.
1. Create an account on the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/).
2. Log in and get your API key from your profile page.
3. Save your API credentials in a `.cdsapirc` file in your home directory (`~/.cdsapirc`).

## Setup Environment

You can set up your virtual environment using either `venv` or `conda`. There is a `requirements.txt` file provided with dependencies. 

### Using venv and pip

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows

# Install the required packages
pip install -r requirements.txt
```

## Running the Notebooks

### Using VS Code (Recommended)
If you are using Visual Studio Code with the Jupyter extension installed, you can simply open the notebooks in the `notebooks/` directory and select your `.venv` as the Python kernel.

### Using the Terminal
If you are running this from a standalone terminal, you will need to install Jupyter to run the notebooks:

```bash
# Install JupyterLab
pip install jupyterlab

# Start the interface
jupyter lab

Once the interface opens in your browser, navigate to the `notebooks/` directory and open one of the provided notebooks:
- `retrieve_and_plot_seaice.ipynb`
- `retrieve_and_plot_subdomain.ipynb`
- `retrieve_and_plot_timeseries.ipynb`
