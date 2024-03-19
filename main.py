import ddddocr
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

ocr = ddddocr.DdddOcr()


@app.route('/api/v1/ocr', methods=['POST'])
def v1Ocr():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return make_response(jsonify({
            'code': 'file.not.found',
            'message': '文件不能为空',
        }
        ), 400)

    file = request.files['file']

    # 检查文件名是否为空
    if file.filename == '':
        return make_response(jsonify({
            'code': 'file.not.found',
            'message': '文件不能为空',
        }
        ), 400)

    # 如果文件存在且符合条件
    if file:
        file_bytes = file.read()
        res = ocr.classification(file_bytes)

        # 构造返回的 JSON 数据
        response = {
            'code': 'ok',
            'message': 'success',
            'data': res
        }

        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
