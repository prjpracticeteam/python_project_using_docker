FROM ubuntu
RUN apt-get update
RUN apt-get install python3 -y
copy . /opt/pythonapp/
WORKDIR /opt/pythonapp/
ENTRYPOINT ["python3"]


CMD [" .\data\L1.txt .\data\L2.txt .\data\R.txt"]+
EXPOSE 8000