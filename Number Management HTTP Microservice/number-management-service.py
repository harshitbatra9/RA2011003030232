import requests
import json
from flask import Flask, request

def get_numbers(urls):
  """Retrieves the numbers from the specified URLs."""
  numbers = []
  for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
      numbers.extend(json.loads(response.content)["numbers"])
  return numbers

def main():
  """Starts the HTTP microservice."""
  app = Flask(__name__)

  @app.route("/numbers")
  def get_numbers_endpoint():
    """Retrieves the numbers from the specified URLs."""
    urls = request.args.getlist("url")
    numbers = get_numbers(urls)
    return json.dumps({"numbers": numbers})

  app.run(port=8008)
if __name__ == "__main__":
  main()
