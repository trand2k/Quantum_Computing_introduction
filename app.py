from flask import Flask, request, jsonify, send_from_directory
import random
import time
import os

app = Flask(__name__)

def lcg_random(seed, a=1664525, c=1013904223, m=2**32):
    """
    Linear Congruential Generator (LCG) for generating pseudo-random numbers.
    """
    while True:
        seed = (a * seed + c) % m
        yield seed

def generate_random_list(n, seed=None):
    """
    Generates a list of 2n unique random positive integers, each using a maximum of n bits,
    and another random positive integer k using n bits. Uses a given seed if provided.
    """
    max_value = 2 ** n - 1  # Maximum value using n bits
    unique_numbers = set()
    if seed is None:
        seed = int(time.time() * 1000) % 2**32  # Use current time if no seed provided
    lcg = lcg_random(seed)
    
    # Generate 2n unique numbers
    while len(unique_numbers) < 2 * n:
        random_number = next(lcg) % max_value + 1
        unique_numbers.add(random_number)
    
    list_n = list(unique_numbers)
    
    # Generate a random k
    k = next(lcg) % max_value + 1
    
    return k, list_n

def search_k(k, list_n):
    """
    Checks if k exists in the list_n.
    Returns (True, n_steps) if k exists, and (False, n_steps) otherwise,
    where n_steps is the number of steps needed.
    """
    # import pdb;pdb.set_trace()
    n_steps = 0
    for num in list_n:
        n_steps += 1
        if num == k:
            return True, n_steps
    return False, n_steps

def less_than_k(k, list_n):
    """
    Finds all integers less than k in the list_n.
    Returns (list_nk, n_steps), where list_nk contains all numbers in list_n that are less than k,
    and n_steps is the number of steps needed.
    """
    list_nk = []
    n_steps = 0
    for num in list_n:
        n_steps += 1
        if num < k:
            list_nk.append(num)
    return list_nk, n_steps

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/generate', methods=['GET'])
def generate():
    n = int(request.args.get('n'))
    seed = request.args.get('seed', default=None, type=int)
    k, list_n = generate_random_list(n, seed)
    return jsonify({
        'k': k,
        'list_n': list_n
    })

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    k = int(data['k'])
    list_n = data['list_n']
    exists, steps = search_k(k, list_n)
    return jsonify({
        'exists': exists,
        'steps': steps
    })

@app.route('/less_than', methods=['POST'])
def less_than():
    data = request.json
    k = int(data['k'])
    list_n = data['list_n']
    list_nk, steps = less_than_k(k, list_n)
    return jsonify({
        'list_nk': list_nk,
        'steps': steps
    })

if __name__ == '__main__':
    app.run(debug=True)
