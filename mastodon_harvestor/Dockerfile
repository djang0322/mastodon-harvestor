FROM python:3

WORKDIR /mastodon_harvestor

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./mastodon_runner.py" ]