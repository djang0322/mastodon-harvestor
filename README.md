# Mastodon Harvester Application

## Overview

The Mastodon Harvester is a cloud-based application designed for harvesting and analyzing social media data from Mastodon servers. This project is part of the **Australia Social Media Analytics on the Cloud** assignment. The application uses CouchDB for storing pre-processed data on harvested data.

## Features

- **Mastodon Data Harvesting**: Collects posts (toots) from multiple Mastodon servers using their APIs.
- **Data Storage**: Utilizes CouchDB to store harvested Mastodon data.

## Technologies Used

- **Backend**: Python with Mastodon.py for data harvesting.
- **Database**: CouchDB with MapReduce for data analytics.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

## Files Overview

- `ansible/*`: Contains set of playbooks used for deploying the app to Melbourne Research Cloub
- `mastodon_harvestor`:
  - `modules`:
    - `constants.py`: Defines constant values used in the app
    - `db_client.py`: Defines CouchDB client to talk to database
    - `mastodon_client.py`: Defines Mastodon client to perform various operations
    - `mastodon_stream_listner.py`: Responsible for talking to Mastodon servers
    - `matodon_tooth.py`: Represent tooth retrieved from the Mastodon servers
  - `mastodon_runner.py`: Starts the app
- `docker-compose.yml`:
  - `couchdb`: Runs CouchDB, exposing port 5984.
  - `mastodon-harvestor`: Runs the Mastodon Harvestor service, which connects to CouchDB.

## Running the Project on Local Machine

1. **Clone the Repository**

Clone this repository to your local machine:
```bash
git clone https://github.com/djang0322/mastodon-harvestor.git
```

### 2. Obtain Mastodon API Access Tokens

Before running the application, obtain access tokens for the Mastodon servers to harvest from:

- **Register an Application on Mastodon:**
  1. Navigate to a Mastodon server’s settings page.
      - [Social](https://mastodon.social)
      - [AU](https://mastodon.au)
      - [Cloud](https://mastodon.cloud)
      - [World](https://mastodon.world)
      - [UK](https://mastodonapp.uk)
  2. Create a new application, providing necessary details such as the application name, website, and required scopes.
  3. After creation, Mastodon will provide you with an **access token**.

### 3. Update the `docker-compose.yml` with Your Tokens

Open the `docker-compose.yml` file in a text editor. Locate the `environment` section under the `mastodon-harvestor` service. Replace placeholder values with your actual Mastodon access tokens:

```yaml
environment:
  MASTODON_ACCESS_TOKEN_SOCIAL: your_social_token_here
  MASTODON_ACCESS_TOKEN_AU: your_au_token_here
  MASTODON_ACCESS_TOKEN_CLOUD: your_cloud_token_here
  MASTODON_ACCESS_TOKEN_WORLD: your_world_token_here
  MASTODON_ACCESS_TOKEN_UK: your_uk_token_here
  DB_URL: "http://couchdb:5984/"
  DB_USERNAME: "admin"
  DB_PASSWORD: "admin"
```

### Run Service

1. Start Service
    ```bash
    docker-compose up
    ```
2. Check CouchDB is running by navigating to http://localhost:5984/_utils/
3. Check Services are running by `docker-compose ps`
