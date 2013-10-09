#!/bin/bash
# find the ip address (this will print all IP address, assume you only have one)
IP_ADDR=$(ifconfig | awk -F':' '/inet addr/&&!/127.0.0.1/{split($2,_," ");print _[1]}')
echo "***Get IP:$IP_ADDR"


curl http://server-dns.eu01.aws.af.cm/your-service-name/to/$IP_ADDR/
echo "\n***Update server IP \n"

MAP_ADDR=$(curl http://server-dns.eu01.aws.af.cm/get/your-service-name/)
echo "***Mapping server:$MAP_ADDR \n"