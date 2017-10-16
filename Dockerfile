FROM python:3-onbuild

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "ratingstrading.app/com/crcapital/main/CRCRatingsMain.py" ]
