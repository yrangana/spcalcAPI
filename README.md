[![Python application test with Github Actions](https://github.com/yrangana/spcalcAPI/actions/workflows/main.yml/badge.svg)](https://github.com/yrangana/spcalcAPI/actions/workflows/main.yml)

# spcalcAPI
Simple FAst API to Strategy Pattern Calculator (spcalc)

## Instructions to install and run the application

1. Clone the repository
```bash
git clone https://github.com/yrangana/spcalcAPI.git
```

2. Install the requirements
```bash
Make install
```

3. Run the application
```bash
python app.py   
``` 

## RESTful API Endpoint

1. Add two numbers
```bash
curl -X 'POST' \
  'http://localhost:8000/calculate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "number1": 10,
  "number2": 10,
  "operation": <operation>
}'
```

supported operations are 
- add
- subtract
- multiply
- divide



## API Documentation

Swagger UI
```bash
http://localhost:8000/docs
```





