from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('threat_templates/stride.json') as f:
    stride_threats = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    components = request.json.get('components', [])
    data_flows = request.json.get('data_flows', [])
    threats = []

    for comp in components:
        for category in stride_threats:
            threats.append({
                "component": comp,
                "threat_type": category,
                "description": stride_threats[category]
            })

    return jsonify({"threats": threats})

if __name__ == '__main__':
    app.run(debug=True)
