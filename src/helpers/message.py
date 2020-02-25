from flask import jsonify

MESSAGE_RESPONSE = {
    10: "Chữ ký bảo mật không hợp lệ",
    11: "Xác thực không hợp lệ",
    12: "Dữ liệu truyền vào không hợp lệ"
}

class Message:

    @staticmethod
    def error(error_code: int, msg_extra: list = []):
        if error_code not in MESSAGE_RESPONSE:
            return jsonify({
                "error": {
                  "code": 99,
                  "message": "có lỗi xảy ra trong quá trình xử lý",
                  "errors": msg_extra
                }
            })

        return jsonify({
            "error": {
              "code": error_code,
              "message": MESSAGE_RESPONSE[error_code],
              "errors":  msg_extra
            }
        })

    @staticmethod
    def success(data, is_extend=True):
        if is_extend == False:
            return jsonify(data)
        return jsonify({
            "success": True,
            "data": data
        })
