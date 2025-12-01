from flask import Flask, jsonify, request
import math

app = Flask(__name__)


def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_square(n):
    """Checks if a number is a perfect square."""
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

TRIVIA_DATA = {
    1: "1 is the first non-zero positive integer.",
    7: "7 is the most common 'lucky' number.",
    21: "21 is the number of spots on a standard die.",
    42: "42 is the 'Answer to the Ultimate Question of Life, the Universe, and Everything' in The Hitchhiker's Guide to the Galaxy.",
    100: "100 is the boiling point of water in Celsius at 1 atmosphere.",
    1337: "1337 is a well-known example of 'leetspeak' for 'elite'.",
    8192: "8192 is a power of 2 (2^13)."
}


def get_generic_trivia(n):
    """Generates a list of simple facts about any number."""
    facts = []
    
    
    if n % 2 == 0:
        facts.append("is an even number")
    else:
        facts.append("is an odd number")
        
    
    if is_prime(n):
        facts.append("is a prime number")
        
    
    if is_square(n):
        root = int(math.sqrt(n))
        facts.append(f"is a perfect square (the square of {root})")
        
    if len(facts) == 1:
        return f"{n} {facts[0]}."
    else:
        return f"{n} " + " and ".join(facts) + "."

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Number Trivia API!",
        "endpoints": [
            {
                "path": "/",
                "method": "GET",
                "description": "Returns available API endpoints"
            },
            {
                "path": "/number/<number>",
                "method": "GET",
                "description": "Returns interesting facts about the given number"
            }
        ],
        "example_requests": [
            "GET /number/42",
            "GET /number/7"
        ]
    })

@app.route('/number/<int:number>')
def get_trivia(number):
    """
    The main API endpoint.
    It takes an integer as part of the URL path and returns a JSON object with a fact.
    Example: /number/42
    """
    if not 1 <= number <= 10000:
        return jsonify({
            "error": "Number out of range. Please use a number between 1 and 10000."
        }), 400  
        
    fact = TRIVIA_DATA.get(number)
    
    if fact is None:
        fact = get_generic_trivia(number)
        
    return jsonify({
        "number": number,
        "fact": fact
    })

if __name__ == '__main__':
    app.run(debug=False)
