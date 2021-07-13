#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
docker build -t uda_cap_hello .
docker build --tag=rluzardo/uda_cap_hello .
docker push rluzardo/uda_cap_hello

# Step 2: 
#docker image ls

# Step 3: 
docker run -p 8000:80 uda_cap_hello