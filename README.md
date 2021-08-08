# Apache_Kafka

# Storing real time user stock data from alpha vantage API to HDFS using Apache Kafka

    Step 1: get the api key by visiting the site https://www.alphavantage.co/support/#api-key

    Step 2: go through the documentation of stock api and get the python code for Time Series Stock APIs

    Step 3: write the python code on a producer.py file and add the api key using the .env file.

    Step 4: write the python code on a consumer.py file to dispaly stock data and create a text file and store the output into it.

    Step 5: now start all servers of hdfs by start-all.sh command and create a directory on hdfs as stock_live_data.

    Step 6: now copy the output file of consumer.py to hdfs by using copyFromLocal command.

    Step 7: now we can see our output or file is successfully written by sink in our hdfs as stock_data

    Video link for this task is : https://youtu.be/asBUv38TE7M
