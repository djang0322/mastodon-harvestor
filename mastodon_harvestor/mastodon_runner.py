from modules.mastodon_client import MastodonClient
from modules.db_client import CouchDBClient
from modules.constants import *
import os
import random

# choose random value from list
def choose_mastodon_site() -> dict:
    return random.choice(MASTODON_SITES)

def main() -> None:
    # mastodon_site = choose_mastodon_site()
    # url = mastodon_site['URL']
    # token = os.environ[mastodon_site['TOKEN']]

    url = MASTODON_SITES[0]['URL']
    token = os.environ[MASTODON_SITES[0]['TOKEN']]
    db_client = CouchDBClient(DB_USERNAME, DB_PASSWORD, DB_URL)
    mastodon_client = MastodonClient(url, token, db_client)
    if (db_client.create_database(TOOTH_DATABASE)):
        mastodon_client.start_public_streaming()

def test() -> None:
    db_client = CouchDBClient(DB_USERNAME, DB_PASSWORD, DB_URL)
    print(db_client.get_all_database())
    print(TOOTH_DATABASE in db_client.get_all_database())

if __name__ == '__main__':
    main()
    # test()