import requests
import time
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data(query="perl", max_retries=3, timeout=5):
    """
    Fetch data from StackExchange API with retries and error handling.
    
    :param query: The search term to query on StackOverflow (default is 'perl').
    :param max_retries: Number of times to retry in case of failure (default is 3).
    :param timeout: Timeout duration in seconds for the request (default is 5).
    :return: List of items (answers) or an empty list if the request fails.
    """
    url = f"https://api.stackexchange.com/2.3/search"
    params = {
        "order": "desc",
        "sort": "activity",
        "intitle": query,
        "site": "stackoverflow"
    }
    
    retries = 0
    while retries < max_retries:
        try:
            logging.info(f"Fetching data with query: {query}, attempt {retries + 1}/{max_retries}")
            response = requests.get(url, params=params, timeout=timeout)
            
            # Si la respuesta es exitosa, procesamos la información
            if response.status_code == 200:
                items = response.json().get('items', [])
                logging.info(f"Fetched {len(items)} items")
                return items
            else:
                logging.warning(f"Received unexpected status code {response.status_code}. Retrying...")
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}. Retrying...")
        
        # Aumentamos el contador de reintentos
        retries += 1
        time.sleep(2 ** retries)  # Exponential backoff, espera más tiempo en cada reintento

    logging.error("Max retries reached. Returning empty list.")
    return []  # Si se alcanza el número máximo de reintentos, retornamos una lista vacía

