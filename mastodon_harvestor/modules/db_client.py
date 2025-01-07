from typing import Any

from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from requests.exceptions import HTTPError


class CouchDBClient():

    def __init__(self, username, password, url) -> None:
        self.username = username
        self.password = password
        self.url = url
    
    def connect(self) -> bool:
        try:
            self.authenticator = CouchDbSessionAuthenticator(self.username, self.password)
            self.client = CloudantV1(authenticator=self.authenticator)
            self.client.set_service_url(self.url)
            print("Connected to DB")
            return True
        except Exception as e:
            print(f"Failed connection to DB:: {e}")
            return False

    def get_session(self) -> dict:
        return self.client.get_session_information().get_result()
    
    def get_all_database(self) -> list:
        return self.client.get_all_dbs().get_result()
    
    def get_all_docs_from_database(self, database) -> list:
        return self.client.post_all_docs(db=database).get_result()
    
    def get_document(self, database, id) -> Any:
        return self.client.get_document(db=database, doc_id=id).get_result()
    
    def update_document(self, database, new_doc) -> Any:
        return self.client.post_document(db=database, document=new_doc).get_result()
    
    def get_client(self) -> CloudantV1:
        return self.client
    
    def create_database(self, database) -> bool:
        if (database in self.get_all_database()):
            return True
        return self.client.put_database(database, partitioned=False).get_result()
    
    def add_document(self, database, doc):
        try:
            return self.client.post_document(db=database, document=doc).get_result()
        except HTTPError as err:
            print(f"HTTPError occured on add_document: {err}")
        except Exception as e:
            print(f"Failed add document: {e}")
            print(e)

    def add_bulk_document(self, database, docs):
        try:
            return self.client.post_bulk_docs(db=database, bulk_docs=docs).get_result()
        except HTTPError as err:
            print(f"HTTPError occured on add_bulk_document: {err}")
            return {}
        except Exception as e:
            print(f"Failed add_bulk_document: {e}")
            print(e)
            return {}
