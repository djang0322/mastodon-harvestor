FROM python:3

WORKDIR /mastodon_harvestor

ENV MASTODON_ACCESS_TOKEN_SOCIAL=""
ENV MASTODON_ACCESS_TOKEN_AU=""
ENV MASTODON_ACCESS_TOKEN_CLOUD=""

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./mastodon_runner.py" ]

EXPOSE 3030