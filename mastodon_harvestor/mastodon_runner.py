from requests.exceptions import ConnectionError
from modules.mastodon_client import MastodonClient
from modules.db_client import CouchDBClient
from modules.constants import *
import os
import sys
import random

# choose random value from list
def choose_mastodon_site() -> dict:
    return random.choice(MASTODON_SITES)

def get_couchDB_client() -> CouchDBClient:
    db_client = CouchDBClient(DB_USERNAME, DB_PASSWORD, DB_URL)
    return db_client

def connect_to_couchDB(db_client: CouchDBClient) -> bool:
    return db_client.connect()

def get_mastodon_client(db_client: CouchDBClient, index: int) -> MastodonClient:
    mastodon_site = None

    if (index == -1):
        mastodon_site = choose_mastodon_site()
    else:
        mastodon_site = MASTODON_SITES[index]

    url = mastodon_site['URL']
    token = os.environ[mastodon_site['TOKEN']]
    mastodon_client = MastodonClient(url, token, db_client)
    return mastodon_client

def main() -> None:
    trial = 0
    index = -1

    if len(sys.argv) > len(MASTODON_SITES):
        print(f'Available index range = 0 to {len(MASTODON_SITES) - 1}')
        exit(0)
    elif len(sys.argv) >= 2:
        index = int(sys.argv[1])

    while trial < 10:
        try:
            mastodon_clinet = None
            db_client = get_couchDB_client()
            connected = connect_to_couchDB(db_client)
            if (connected and db_client.create_database(TOOTH_DATABASE)):
                mastodon_client = get_mastodon_client(db_client, index)
                mastodon_client.start_public_streaming()
        except Exception as e:
            print(f"Accounted Error {trial} times: {e}")
            if mastodon_clinet != None:
                mastodon_client.close_stream()
            index += 1
            trial += 1

if __name__ == '__main__':
    main()