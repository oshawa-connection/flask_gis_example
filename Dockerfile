FROM python:3
# In reality this would be 80 and 443
EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]