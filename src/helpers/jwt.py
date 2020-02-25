from flask import g as global_context
import jwt
import os

class JWT:

    @staticmethod
    def auth(token: str) -> bool:
        try:
            result = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=["HS256"])    
            if "phone_number" not in result:
                return False
            global_context.phone_number = result["phone_number"]
            return True
        except Exception as e:
            return  False

