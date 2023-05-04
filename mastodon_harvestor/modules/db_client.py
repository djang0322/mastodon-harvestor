from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from requests.exceptions import HTTPError
from modules.constants import *

class CouchDBClient():

    def __init__(self, username, password, url):
        self.authenticator = CouchDbSessionAuthenticator(username, password)
        self.client = CloudantV1(authenticator=self.authenticator)
        self.client.set_service_url(url)

    def get_session(self) -> dict:
        return self.client.get_session_information().get_result()
    
    def get_all_database(self) -> list:
        return self.client.get_all_dbs().get_result()
    
    def get_client(self) -> CloudantV1:
        return self.client
    
    def create_database(self, database) -> bool:
        if (database in self.get_all_database()):
            return True
        return self.client.put_database(database, partitioned=False).get_result()
    
    def add_document(self, database, doc) -> None:
        try:
            response = self.client.post_document(db=database, document=doc).get_result()
            return response
        except HTTPError as err:
            print(f'HTTPError occured on add_document: {err}')
        except Exception as e:
            print(f'Failed add document')
            print(e)

    def add_bulk_document(self, database, docs) -> dict:
        try:
            response = self.client.post_bulk_docs(db=database, bulk_docs=docs).get_result()
            return response
        except HTTPError as err:
            print(f'HTTPError occured on add_bulk_document: {err}')
        except Exception as e:
            print(f'Failed add_bulk_document')
            print(e)
