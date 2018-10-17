# -*- coding: utf-8 -*-
from pusher import Pusher


class Permissions:
    ROOM_SCOPE = "room"
    GLOBAL_SCOPE = "global"

    JOIN_ROOM = "room:join"
    LEAVE_ROOM = "room:leave"
    ADD_ROOM_MEMBER = "room:members:add"
    REMOVE_ROOM_MEMBER = "room:members:remove"
    CREATE_ROOM = "room:create"
    DELETE_ROOM = "room:delete"
    UPDATE_ROOM = "room:update"
    CREATE_MESSAGE = "message:create"
    CREATE_TYPING_EVENT = "room:typing_indicator:create"
    SUBSCRIBE_PRESENCE = "presence:subscribe"
    UPDATE_USER = "user:update"
    GET_ROOM_MESSAGES = "room:messages:get"
    GET_USER = "user:get"
    GET_ROOM = "room:get"
    GET_USER_ROOMS = "user:rooms:get"
    CREATE_FILE = "file:create"
    GET_FILE = "file:get"

    VALID_PERMISSIONS = {
        'room': [
            JOIN_ROOM,
            LEAVE_ROOM,
            ADD_ROOM_MEMBER,
            REMOVE_ROOM_MEMBER,
            DELETE_ROOM,
            UPDATE_ROOM,
            CREATE_MESSAGE,
            CREATE_TYPING_EVENT,
            GET_ROOM_MESSAGES,
            CREATE_FILE,
            GET_FILE
        ],
        'global': [
            JOIN_ROOM,
            LEAVE_ROOM,
            ADD_ROOM_MEMBER,
            REMOVE_ROOM_MEMBER,
            CREATE_ROOM,
            DELETE_ROOM,
            UPDATE_ROOM,
            CREATE_MESSAGE,
            CREATE_TYPING_EVENT,
            SUBSCRIBE_PRESENCE,
            UPDATE_USER,
            GET_ROOM_MESSAGES,
            GET_USER,
            GET_ROOM,
            GET_USER_ROOMS,
            CREATE_FILE,
            GET_FILE
        ]
    }


class Client:
    pass


class Chatkit:
    client = Client()

    def __init__(self, **kwargs):
        base_options = {
            'locator': kwargs.get('instance_locator'),
            'key': kwargs.get('key'),
            'port': kwargs.get('port'),
            'host': kwargs.get('host'),
            'client': kwargs.get('client')
        }

        self.api_instance = Pusher({**base_options,
                                    **{'service_name': 'chatkit', 'service_version': 'v1'}})
        self.authorizer_instance = Pusher({**base_options,
                                           **{'service_name': 'chatkit_authorizer', 'service_version': 'v1'}})

    def authenticate(self, request, **kwargs):
        return self.api_instance.authenticate(request, kwargs)

    def generate_access_token(self, **kwargs):
        return self.api_instance.generate_access_token(kwargs)

    # User API
    def create_user(self, id, name, avatar_url, custom_data):
        pass

    def delete_user(self, id):
        pass

    def get_users(self, from_id):
        pass

    def get_users_by_ids(self, user_ids):
        pass

    # Room API
    def get_room(self, room_id):
        pass

    def get_room_messages(self, room_id, initial_id, direction, limit):
        pass

    def get_rooms(self, from_id):
        pass

    # Authorizer API
    def create_room_role(self, name, permissions):
        return self._create_role(name, Permissions.ROOM_SCOPE, permissions)

    def create_global_role(self, name, permissions):
        return self._create_role(name, Permissions.GLOBAL_SCOPE, permissions)

    def delete_room_role(self, role_name):
        return self._delete_role(role_name, Permissions.ROOM_SCOPE)

    def delete_global_role(self, role_name):
        return self._delete_role(role_name, Permissions.GLOBAL_SCOPE)

    def assign_global_role_to_user(self, user_id, role_name):
        return self._assign_role_to_user(user_id, role_name, None)

    def assign_room_role_to_user(self, user_id, role_name, room_id):
        return self._assign_role_to_user(user_id, role_name, room_id)

    def get_roles(self):
        pass

    def get_user_roles(self, user_id):
        pass

    def remove_global_role_for_user(self, user_id):
        return self._remove_role_for_user(user_id, None)

    def remove_room_role_for_user(self, user_id, room_id):
        return self._remove_role_for_user(user_id, room_id)

    def get_permissions_for_global_role(self, role_name):
        return self._get_permissions_for_role(role_name, Permissions.GLOBAL_SCOPE)

    def get_permissions_for_room_role(self, role_name):
        return self._get_permissions_for_role(role_name, Permissions.ROOM_SCOPE)

    def update_role_permissions(self, role_name, scope, permissions_to_add, permissions_to_remove):
        self._check_permissions(permissions_to_add + permissions_to_remove)

    def _create_role(self, name, scope, permissions):
        pass

    def _delete_role(self, role_name, scope):
        pass

    def _assign_role_to_user(self, user_id, role_name, room_id):
        pass

    def _remove_role_for_user(self, user_id, room_id):
        pass

    def _get_permissions_for_role(self, role_name, scope):
        pass

    def _check_permissions(self, permissions):
        pass













