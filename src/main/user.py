from flask import Flask, render_template

app = Flask(__name__)

# サンプルデータ
sample_data = [
    {
        'userName': 'TEST1',
        'mail': 'abc@xxx.xx',
        'divisionName': 'ABC',
        'branchName': '東京支店',
        'regionName': '東日本',
        'authority': '管理者',
        'userNo': '000001',
        'createdDate': '2025/11/05',
        'modifiedDate': '2025/11/11',
    }
]

@app.route('/')
def index():
    return render_template('index.html', data=sample_data)

@app.route('/search', methods=['POST'])
def search():
    # 検索機能は実装せず、サンプルデータをそのまま返す
    return render_template('index.html', data=sample_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
