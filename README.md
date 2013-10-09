server-DNS
==========

## A Django template for Appfog server

Check the instance running on the Appfog: http://server-dns.eu01.aws.af.cm/

Based on Django 1.4 & MySQL 

### Functions

keyword storage for IP address based on the service name
keyword search based on the service name


add/update a service: http://server-dns.eu01.aws.af.cm/service-name/to/IP-address

FEEDBACK: create or update

search a service: http://server-dns.eu01.aws.af.cm/get/service-name

FEEDBACK: IP adress or 404

Database table:
service-name, IP-address, create/update date

### Potential Usage

Local network server/peer lookup (That is why I build this)

### Folder structure

serverdns folder include all Django source code with sub-directory strucutre

script folder include a Shell script, which can be used to create/update its IP-address



