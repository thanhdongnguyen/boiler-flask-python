from flask import request
from src.config.logger import Logger
from src.controllers.member_controller import Member_controller
from src.helpers.message import Message


class Routes:
    
    def __init__(self, app):
        self.app = app
        self.logger = Logger()
        self.member_controller = Member_controller()

    def v1(self):
        
        version = "v1"
        @self.app.route("/{}/list/user".format(version), methods=["GET"])
        def get_list_user():
            input = request.values
            sort = False if 'sort' not in input or input["sort"] not in ["asc", "desc"] else input["sort"] 
            return self.member_controller.get_list_member(sort)

        @self.app.route("/{}/user/create".format(version), methods=["POST"])
        def create_user():
            input = request.values
            self.logger.info(input)
            if "username" not in input or "phone_number" not in input:
                return Message.error(12)
            self.member_controller.create_user(input["username"], input["phone_number"])
            return Message.success({"success": True}, False)

        @self.app.route("/{}/user/edit".format(version), methods=["POST"])
        def edit_user():
            input = request.values
            if "phone_number" not in input or "username" not in input:
                return Message.error(12)
            self.member_controller.update_user(input["phone_number"], input["username"])
            return Message.success({"success": True}, False)


        @self.app.route("/{}/user/delete".format(version), methods=["POST"])
        def delete_user():
            input = request.values

            if "phone_number" not in input:
                return Message.error(12)
            self.member_controller.delete_user(input["phone_number"])
            return Message.success({"success": True}, False)
        
        @self.app.route("/{}/user/get".format(version), methods=["GET"])
        def get_info_user():
            input = request.values 
            sort = False if 'sort' not in input or input["sort"] not in ["asc", "desc"] else input["sort"] 

            if "phone_number" not in request.values:
                return Message.get(11)
            result = self.member_controller.get_first_member(sort, input["phone_number"])

            return result

        @self.app.route("/{}/poll/get".format(version), methods=["GET"])
        def get_poll():
            pass

        @self.app.route("/{}/poll/create".format(version), methods=["POST"])
        def save_poll():
            input = request.values
            pass

        @self.app.route("/{}/poll/result".format(version), methods=["GET"])
        def get_poll_result():
            input = request.values
            pass
