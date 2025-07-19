# Alexupport - Amazon Product Support Assistant

🤖 An autonomous AI agent built with LangChain that provides customer support for Amazon products using real customer Q&A data and verified information.

## Agent structure & workflow

The Alexupport agent is comprised of several microagents in the `agents` directory:

* **Input Refiner microagent**: Implemented in the `input_refiner.py` file, this microagent refines the user input by ___
* **Information Retriever microagent**: Implemented in the `information_retrever.py` file, this microagent retrieves the relevant data from the Qdrant vectorstore by comparing it to the (refined) user input.
* **Is-Answerable microagent**: Implemented in the `is_answerable_agent.py` file, this microagent determines if the (refined) input question can be answered using the retrieved data.

The above components create the complete Alexupport workflow - given a user question, the Alexupport agent:

1. asdf
2. asdf
3. asdf
4. asdf
5. asdf
6. asdf

## Setup

1. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2. **Set the AzureOpenAI `API_KEY` environment variable in the `.env` file**
    ``` bash
    echo "API_KEY = <your-api-key>" > .env
    ```

3. **Run the agent**
    ```bash
    python main.py
    ```