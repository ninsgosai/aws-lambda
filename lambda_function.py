import re
from typing import Dict, Any

def process_log_file(log_content: str) -> Dict[str, Any]:
    """
    Analyzes log entries and extracts error patterns.

    Args:
        log_content (str): A string containing log entries.

    Returns:
        Dict[str, Any]: A dictionary containing the total number of errors 
                        and a list of unique error messages.
    """
    if not log_content.strip():
        # Handle empty log content
        return {"total_errors": 0, "unique_error_messages": []}

    try:
        # Regular expression to parse log entries and extract error messages
        error_pattern = r"^\[.*?\] ERROR: (.+)$"
        matches = re.findall(error_pattern, log_content, re.MULTILINE)
        
        total_errors = len(matches)
        unique_error_messages = sorted(set(matches))
        
        return {
            "total_errors": total_errors,
            "unique_error_messages": unique_error_messages
        }
    except Exception as e:
        # Error handling
        raise ValueError(f"Failed to process log content: {e}")

def lambda_handler(event, context):
    """
    AWS Lambda handler to process log files.
    
    Args:
        event (dict): Input event containing candidate_id and log_content.
        context (object): AWS Lambda runtime information.

    Returns:
        dict: Response containing status code and results.
    """
    try:
        candidate_id = event.get("candidate_id", "unknown")
        log_content = event.get("log_content", "")
        
        # Process the log content
        result = process_log_file(log_content)
        
        # Return the result
        return {
            "statusCode": 200,
            "body": {
                "candidate_id": candidate_id,
                "result": result
            }
        }
    except Exception as e:
        # Handle unexpected errors
        return {
            "statusCode": 500,
            "body": {
                "error": str(e)
            }
        }
