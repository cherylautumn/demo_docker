1. Make base docker which include basic functions

create a folder: 
create a dockerfile
$ docker build -t cherylq/base:v0 .

$ docker push cherylq/base

$ docker run -d -P --name test_sshd cherylq/base:v0

cheryltekiMacBook-Pro-2:docker-base cheryl$ docker port test_sshd 22
0.0.0.0:32768

cheryltekiMacBook-Pro-2:docker-base cheryl$ docker-machine ip default
192.168.99.100

cheryltekiMacBook-Pro-2:docker-base cheryl$ ssh root@192.168.99.100 -p 32768

Clean up
$ docker stop test_sshd

$ docker rm test_sshd

$ docker rmi eg_sshd

docker exec -it lileedocker_zookeeper_1 sh

Docker Folder /Users/cheryl/DevWorkSpace/lilee_code/lilee_docker
1. build img
- $ docker build -t cherylq/base:v0 .
- $ docker build -t cherylq/:zookeeper .
- $ docker build -t cherylq/kafka:v0 .

2. docker-compose up
3. python3 exmaple.py
4. docker-compose stop
5. docker-compose rm

