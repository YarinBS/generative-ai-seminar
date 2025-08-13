"""
This module defines the InformationRetriever microagent,
which is responsible for retrieveing relevant information from the Qdrant database.
"""

from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

from agent.llm_client import LLMClient

QDRANT_URL = "https://63ad19dc-7779-4868-bc81-41f5fae4353a.europe-west3-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0._mnughDNgXpg2I_tMDwpIIKZJiDqma2o_YDld0ZseR4"
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

class InformationRetriever:
    """Microagent for retrieving relevant information from the Qdrant database."""

    def __init__(self, qdrant_client: QdrantClient, llm_client: LLMClient):
        self.qdrant_client = qdrant_client
        self.llm_client = llm_client

    # def _create_and_populate_collection(self):
    #     """If the collection does not exist, create and populate it"""

    #     if not self.qdrant_client.collection_exists("data_collection"):
    #         # The collection does not exist - create it
    #         self.qdrant_client.create_collection(
    #             collection_name="data_collection",
    #             vectors_config={
    #                 "questionText": {"size": 1536, "distance": Distance.COSINE}
    #             },
    #             # Explicitly index the "asin" field in the payload
    #             payload_schema={
    #                 "asin": {"type": "keyword"}
    #             }
    #         )

    #         # Then, populate the collection
    #         # TODO: Populate the collection with data
    #         raise NotImplementedError("Data population logic is not implemented yet.")

    def retrieve_information(self, query: str, product_id: str) -> list:
        """
        Retrieve relevant information from the Qdrant database based on the user's query.

        Parameters:
        - query (str): The user's question or query.
        - product_id (str): The product ID (ASIN) to filter results.

        Returns:
        - list: A list of relevant documents or snippets related to the query and product ID.
        """

        query_vector = self.llm_client.generate_embeddings(texts=[query])

        # Use the Qdrant client to perform the search
        search_results = client.query_points(
            collection_name="data_collection",  # Collection name to search in
            query=query_vector,  # The vector to search for similar points
            using="questionText",  # The field to use for similarity search
            limit=10,  # Limit the number of results to 10
            with_payload={"exclude": ["asin"]},  # Exclude 'asin' from the result, already known
            query_filter=Filter(  # Filter to narrow down results based on a specific 'asin'
                must=[
                    FieldCondition(key="asin", match=MatchValue(value=product_id)),
                    FieldCondition(key="_score", range={"gte": 0.7})
                ]
            )
        )

        results_answers_and_review_snippets = [result.payload['answers'] + result.payload['review_snippets'] for result in search_results.points]
        return results_answers_and_review_snippets
