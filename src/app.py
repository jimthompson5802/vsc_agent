from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echo', methods=['POST'])
def echo():
    user_input = request.json.get('user_input', '')
    echoed_text = f"echoed: {user_input}"
    return jsonify({'echoed_text': echoed_text})

@app.route('/clear', methods=['POST'])
def clear():
    return jsonify({'echoed_text': '', 'user_input': ''})

if __name__ == '__main__':
    app.run(debug=True)