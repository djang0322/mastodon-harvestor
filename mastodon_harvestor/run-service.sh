#!/usr/bin/env bash
docker service create --name mastodon-harvestor --publish published=5984,target=5984 --replicas 3 --env MASTODON_ACCESS_TOKEN_SOCIAL=Hjv8XHIQMo042o7nTXbWC15WkUtWUd9bekh6s5lz-L0 --env MASTODON_ACCESS_TOKEN_AU=pwvGgbL4Kapd2kYQGTWd20ZqcHP0lTqR9ioyDNlihPo --env MASTODON_ACCESS_TOKEN_CLOUD=B0T98uen8Mt4I-xygsG_CVX3e54m1DFGJMUdpjRXZq4 --env MASTODON_ACCESS_TOKEN_WORLD=bGflW2L837cKzBEb36_8Hl6SuGQ0d6AaWgrsrx7ij3I --env MASTODON_ACCESS_TOKEN_UK=Ep6V4XkMGxFtokagetZAffCotR9ZVk-7Nffto-Oio3k --env DB_URL="http://172.26.134.93:5984/" --env DB_USERNAME="admin" --env DB_PASSWORD="admin" djang9303/mastodon-harvestor:1.5