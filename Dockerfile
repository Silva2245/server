FROM ubuntu
RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install python3-scapy python3-bs4 -y