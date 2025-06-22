import os
from pathlib import Path
from typing import Dict, Any, Optional

def format_search_results(results: Dict[str, Any]) -> str:
    """Format search results into a readable string."""
    if not results or 'organic' not in results:
        return "No search results found."
    formatted = []
    for result in results['organic']:
        formatted.append(f"Title: {result.get('title', 'N/A')}")
        formatted.append(f"Link: {result.get('link', 'N/A')}")
        formatted.append(f"Snippet: {result.get('snippet', 'N/A')}")
        formatted.append("-" * 80)
    return "\n".join(formatted)

def ensure_directory_exists(directory: str) -> Path:
    """Ensure that a directory exists, create it if it doesn't."""
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Get an environment variable with a default value."""
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Required environment variable {key} is not set")
    return value