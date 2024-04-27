FROM python:3.12.2

WORKDIR /opt/app

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/dpkp/kafka-python.git

COPY . .

#CMD ["python", "app.py"]