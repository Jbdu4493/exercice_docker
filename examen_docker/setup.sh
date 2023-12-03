#/bin/bash

working_directory=`pwd`
#Creation du network dedié
echo $working_directory

docker network create --subnet 172.50.0.0/16 --gateway 172.50.0.1 test_api_network

#contruction de toute les images
cd $working_directory/test_authentication
docker image build . -t test_authentication:latest

cd $working_directory/test_authorization
docker image build . -t test_authorization:latest

cd $working_directory/test_content
docker image build . -t test_content:latest

cd $working_directory
docker-compose up

docker container rm -f datascientest_fastAPI
docker image rm -f test_authorization test_content test_authentication datascientest_fastAPI
