from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    text = data.get('text', '')
    return jsonify({"echoed_text": f"echoed: {text}"})

@app.route('/clear', methods=['POST'])
def clear():
    return jsonify({"echoed_text": ""})

if __name__ == '__main__':
    app.run(debug=True)