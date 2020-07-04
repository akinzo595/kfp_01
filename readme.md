

1. conda create -n kf-pipeline

2. conda activate kf-pipeline

3. pip install -r requirements.txt



#Grabing Sample Data from Chicago TaxiCab
select 100k records -> `curl --get 'https://data.cityofchicago.org/resource/wrvz-psew.csv' --data-urlencode '$limit=100000' | tr -d '"' > taxi_data.csv`