def process_flow(data: dict) -> dict:             # Example of high cognitive complexity
  result = {}
  if 'type' in data:
    if data['type'] == 'A':
      if 'value' in data:
        if isinstance(data['value'], (int, float)):
          result['processed'] = data['value'] * 2
        else:
          result['error'] = 'Invalid value type'
      else:
        result['error'] = 'Missing value'
    elif data['type'] == 'B':
      if 'value' in data:
        if isinstance(data['value'], str):
          result['processed'] = data['value'].upper()
        else:
          result['error'] = 'Invalid value type'
      else:
        result['error'] = 'Missing value'
  else:
    result['error'] = 'Missing type'
  return result

# Constants mixed with code
MAX_RETRIES=3                                     # Missing space around operator
DEFAULT_TIMEOUT=30
api_key="your-api-key-here"                       # Security issue: Hardcoded credentials
