#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
docker build -t udacap_green .
docker build --tag=rluzardo/udacap_green .
docker push rluzardo/udacap_green

# Step 2: 
#docker image ls

# Step 3: 
#docker run -p 8000:80 udacap_green