FROM python:3

WORKDIR /mastodon_harvestor

ENV MASTODON_ACCESS_TOKEN_SOCIAL="Hjv8XHIQMo042o7nTXbWC15WkUtWUd9bekh6s5lz-L0"
ENV MASTODON_ACCESS_TOKEN_AU="pwvGgbL4Kapd2kYQGTWd20ZqcHP0lTqR9ioyDNlihPo"
ENV MASTODON_ACCESS_TOKEN_CLOUD="B0T98uen8Mt4I-xygsG_CVX3e54m1DFGJMUdpjRXZq4"

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./mastodon_runner.py" ]