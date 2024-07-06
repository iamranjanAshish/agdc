# Imports
import pandas as pd
import numpy as np
import requests
import faostat as fs
from bs4 import BeautifulSoup
import yaml

rng = np.random.default_rng()

# Configuration File
with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
print('config.yaml loaded successfully...')

# USDA API
if len(cfg['API']) != 0:
    API_KEY = cfg['API']
else:
    # API Encryption
    valid_pass = ['B3x7L5zC', 'K7l2M4pX', 'A7d4L3pN', 'S9l5X2pR', 'C2m8Q6rV']
    receive = False
    while not receive:
        random_vp = valid_pass[rng.integers(len(valid_pass))]
        response = requests.post('https://apiencrypted.000webhostapp.com/', 
                                 data={'vp':random_vp})
        if response.ok:
            source = requests.get('https://apiencrypted.000webhostapp.com/')
            soup = BeautifulSoup(source.text, 'html.parser')
            
            tag = soup.find('p', attrs={'class':random_vp})
            key = tag.get('id')
            API_KEY = key
            receive = response.ok
            
# API Authentication
test = requests.get(f'https://api.ers.usda.gov/data/arms/state?api_key={API_KEY}')

if not test.ok:
    raise ValueError('Invalid API')

print('API authentication successful...')

# Variables
var_info = pd.read_csv('variables_info.csv')
var_info.set_index('id', inplace=True)

# Codes
ld = fs.list_datasets_df()
domain_id = ld[['code', 'label']]
domain_id.set_index('code', inplace=True)

# Error Logging

# Invalid variable_id
id_set = set(var_info.index.to_list())
given_id_set = set(cfg['id'])

if not given_id_set.issubset(id_set):
    raise ValueError('Invalid ID/IDs')

print('No Error was found in variable_ids...')

# Invalid code
code_set = set(domain_id.index.to_list())
given_code_set = set(cfg['codes'])

if not given_code_set.issubset(code_set):
    raise ValueError('Invalid Code/Codes')

print('No Error was found in codes...')

# Missing Values
for param in cfg.keys():
    if param == 'API':
        continue
    if cfg[f'{param}'] == None or len(cfg[f'{param}']) == 0:
        raise ValueError(f"Values were not provided for '{param}'")

# TypeError
for year in cfg['YEAR']:
    if type(year) != int:
        raise TypeError(f"expected 'int' but found {type(year)} for values in YEAR")

print('No Error was found in Inputs...')

# Retrieving data from USDA 
# Every report for each given variable_id for each given year.
print('Retrieving data from USDA...')

for year in cfg['YEAR']:
    for v_id in cfg['id']:
        reports_list = var_info.report.loc[var_info.index==v_id].to_list()
        for report in reports_list:

            out = requests.get(
                f'https://api.ers.usda.gov/data/arms/surveydata?api_key={API_KEY}', 
                params= {
                    "year": [year],
                    "report": report,
                    "variable": v_id,
                }
            )

            df = pd.DataFrame(out.json()['data'], columns=['stat_Year','report_name','report_Dim',
                                                           'category', 'categoryValue',
                                                           'serie_Element_Dim', 'estimate',
                                                           'variableUnit', 'statistic', 
                                                           'median','rse']).sort_values('category')

            df['serie_Element_Dim'] = df.serie_Element_Dim.apply(lambda x: x['desc'])
            df['report_name'] = df.report_Dim.apply(lambda x: x['header'])
            df['report_Dim'] = df.report_Dim.apply(lambda x: x['description'])

            df.rename({'stat_Year':'Year', 'variableUnit':'Unit', 'category' : 'Category', 
                      'categoryValue' : 'Category_Value', 'serie_Element_Dim': 'Category_Description', 
                      'estimate' : 'Estimate', 'median':'Median', 'statistic':'Statistic', 
                       'rse': 'RSE', 'report_Dim':'Report_Description', 'report_name':'Report_Name'}, 
                       axis='columns', inplace=True)

            df.reset_index(inplace=True)
            df.drop('index', inplace=True, axis=1)
            df.to_csv(f'data_csv/{year}_{v_id}_{report}_USDA.csv', index=False)

print('USDA data retrieval successful...')

# Retrieving data from FAO
# Report for each given year for each given code
print('Retrieving data from FAO...')

for code in cfg['codes']:
    params = {'area': fs.get_par(code, 'area')['United States of America'], 
              'year' : cfg['YEAR']}
    data = fs.get_data_df(code, pars=params)
    name = domain_id.label.loc[domain_id.index==code].item()
    data.to_csv(f'data_csv/{name}_FAOSTAT.csv', index=False)

print('FAO data retrieval successful...')

# Confirmation
print('Done:)')
