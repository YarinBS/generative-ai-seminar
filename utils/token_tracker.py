import os
import datetime

def log_token_usage(operation: str, input_tokens: int, output_tokens: int = 0) -> None:
    """Logs the token usage to the total_tokens.txt file"""

    if operation not in ["chat", "embedding"]:
        raise ValueError("Operation must be either 'chat' or 'embedding'.")

    with open("../tokens_count/total_tokens.txt", "a") as file:
        timestamp = datetime.datetime.now().isoformat()
        file.write(f"{timestamp} - {operation}: input={input_tokens}, output={output_tokens}\n")
