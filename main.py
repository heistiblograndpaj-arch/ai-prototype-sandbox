import json
import config

def simulate_llm_call(prompt: str):
    """Simulates a localized payload structure for testing pipeline formats."""
    print(f"[Sandbox] Initializing request with model: {config.DEFAULT_MODEL}")
    
    # Mock payload structure
    payload = {
        "model": config.DEFAULT_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    print(f"[Sandbox] Sending structured payload... Timeout set to {config.API_TIMEOUT}s")
    return {"status": "success", "response": f"Processed: {prompt[:20]}..."}

if __name__ == "__main__":
    test_prompt = "Format the raw system logs into a clean JSON array."
    result = simulate_llm_call(test_prompt)
    print(f"[Result]: {json.dumps(result)}")
