FROM nginxdemos/hello

## Step 1:
WORKDIR /app

## Step 2:

RUN touch hello_logs.txt
RUN echo "checking"

#Install diagnostic tools:
#RUN apt-get update && apt-get install -y vim curl git sudo lsof

## Step 3:
#RUN pip install --no-cache-dir -r requirements.txt
# hadolint ignore=DL3013

## Step 4:
EXPOSE 80
