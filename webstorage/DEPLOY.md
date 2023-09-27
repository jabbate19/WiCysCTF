# Deployment

## Requirements
- Docker

## Environment Variables needed to set
- SERVER_NAME : The domain/port intended

## Steps

- `docker build -t webstorage .`
- `docker run -d -p PORT:8080 webstorage`

