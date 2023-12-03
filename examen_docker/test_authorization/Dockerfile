FROM ubuntu:18.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
RUN mkdir /home/logs/
ADD test.py /home/sources/test.py
WORKDIR /home/sources/
CMD python3 test.py