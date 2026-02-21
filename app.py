from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple in-memory storage for the latest scores
game_data = {"team_a": 0, "team_b": 0}

@app.route('/')
def index():
    return render_template('index.html')

# This is the API endpoint that accepts inputs
@app.route('/update_score', methods=['POST'])
def update_score():
    global game_data
    data = request.json
    if data:
        game_data['team_a'] = data.get('team_a', 0)
        game_data['team_b'] = data.get('team_b', 0)
    return jsonify(game_data)

# API endpoint to get current scores
@app.route('/api/get_score', methods=['GET'])
def get_score():
    return jsonify(game_data)


# API endpoint to reset scores
@app.route('/api/reset_score', methods=['POST'])
def reset_score():
    global game_data
    game_data = {"team_a": 0, "team_b": 0}
    return jsonify(game_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
