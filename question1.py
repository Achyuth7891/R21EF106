from flask import Flask, jsonify
import requests
from collections import deque
import time

app = Flask(__name__)

# Constants
THIRD_PARTY_SERVER_URL = 'http://20.244.56.144/test/rand'
WINDOW_SIZE = 10
TIMEOUT = 0.5

stored_numbers = deque(maxlen=WINDOW_SIZE)

def fetch_numbers_from_server():
    try:
        response = requests.get(THIRD_PARTY_SERVER_URL, timeout=TIMEOUT)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching numbers from server: {e}")
        return []

@app.route('/numbers/<numberid>', methods=['GET'])
def process_number_id(numberid):
    start_time = time.time()

    numbers = fetch_numbers_from_server()

    if not numbers:
        return jsonify({'error': 'Failed to fetch numbers from the server'}), 500

    stored_numbers.extend(numbers)
    unique_numbers = list(set(stored_numbers))

    window_prev_state = list(stored_numbers)[-WINDOW_SIZE:] if len(stored_numbers) > WINDOW_SIZE else []
    window_curr_state = list(unique_numbers)

    average = sum(unique_numbers[-WINDOW_SIZE:]) / len(unique_numbers[-WINDOW_SIZE:]) if unique_numbers else 0

    end_time = time.time()
    elapsed_time = end_time - start_time

    response = {
        'windowPrevState': window_prev_state,
        'windowCurrState': window_curr_state,
        'numbers': numbers,
        'avg': average
    }

    if elapsed_time > TIMEOUT:
        return jsonify({'error': 'Response time exceeded 500ms'}), 500

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=9876)