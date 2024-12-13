from flask import Blueprint, request
from dicepy import roll_dice

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/roll', methods=['POST'])
def roll():
    try:
        numDice = int(request.form['n'])
        if numDice < 1 or numDice > 100:
            return 'Parameter n must be between 1 and 100', 400
    except:
        return 'Parameter n must be a positive integer between 1 and 100', 400
    
    try:
        sides = int(request.form['sides'])
        if sides < 2 or sides > 100:
            return 'Parameter sides must be an integer between 2 and 100', 400
    except:
        return 'Parameter sides must be an integer between 2 and 100', 400

    res = roll_dice(numDice, sides)
    return res.to_dict()
