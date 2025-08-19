"""
Main file to run Alexupport in no-GUI mode
"""

from qdrant_client import QdrantClient

from agent.alexupport_agent import AlexupportAgent


QDRANT_URL = "https://63ad19dc-7779-4868-bc81-41f5fae4353a.europe-west3-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0._mnughDNgXpg2I_tMDwpIIKZJiDqma2o_YDld0ZseR4"
COLLECTION_NAME = "data_collection"

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
points = client.scroll(collection_name=COLLECTION_NAME, limit=2000)[0]

# Extract unique ASINs and map to product titles
asin_title_map = {}
asin_list = sorted({point.payload['asin'] for point in points})


def main():
    """Main entry point for the Alexupport agent (No GUI)."""
    agent = AlexupportAgent()
    print(agent.get_agent_introduction())

    selected_asin = input("Enter a product ID: ")

    # Check if the product ASIN exists in the database
    while selected_asin not in asin_list:
        print("Product ID not found. Please enter a valid product ID.")
        selected_asin = input("Enter a product ID: ")

    # Find the product title for the selected ASIN
    product = next((point for point in points if point.payload.get('asin') == selected_asin), None)
    product_title = product.payload['productTitle'] if product else 'No title found'

    print(f"Selected product: {product_title}")
    user_query = input("Enter your query: ")

    agent.answer_user_query(
        user_query=user_query,
        product_asin=selected_asin
    )

if __name__ == "__main__":
    main()
