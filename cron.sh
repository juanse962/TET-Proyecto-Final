wget https://raw.githubusercontent.com/juanse962/TET-Proyecto-Final/main/covid.csv && 
aws s3 cp covid.csv s3://curso-tet/Raw/covid.csv && rm -rf covid.csv