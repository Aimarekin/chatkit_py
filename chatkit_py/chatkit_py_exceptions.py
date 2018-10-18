# -*- coding: utf-8 -*-
import requests

class Exceptions:
    class Timeout:
        """Exception raised when the timeout is reached when connecting to Chatkit."""
        def __init__(self, request, code, history):
            self.request = request
            self.code = code
            self.history = history
        def __unicode__(self):
            return f"{self.code}: Timeout reached when connecting to Chatkit."
    class AuthenticationError:
        """Exception raised when authenticating into Chatkit fails, probably because of a wrong token."""
        def __init__(self, request, code, history):
            self.request = request
            self.code = code
            self.history = history
        def __unicode__(self):
            return f"{self.code}: Authentication error while connecting to Chatkit, please verify your token."
    class MalformedRequest:
        """Exception raised when a request's body is malformed."""
        def __init__(self, request, code, history):
            self.request = request
            self.code = code
            self.history = history
        def __unicode__(self):
            return f"{self.code}: Request body to Chatkit is malformed, please check data is valid and contact timnockwood@gmx.com if the error's not your fault!"
    class Forbidden:
        """Exception raised when the user requesting the Chatkit resource is not authorized to access it."""
        def __init__(self, request, code, history):
            self.request = request
            self.code = code
            self.history = history
        def __unicode__(self):
            return f"{self.code}: Forbidden. You are not authorized to access this Chatkit resource."
    class NotFound:
        """Exception raised when the requested Chatkit resource does not exist. 404 error."""
        def __init__(self, request, code, history):
            self.request = request
            self.code = code
            self.history = history
        def __unicode__(self):
            return f"{self.code}: This Chatkit resource does not exist."
    class TryLater:
        """Exception raised when a 5xx error is returned by Chatkit. You should try again later."""
        def __init__(self, request, code, history):
            self.request = request
            self.code = code
            self.history = history
        def __unicode__(self):
            return f"{self.code}: 5xx error, according to Chatkit docs ( https://docs.pusher.com/chatkit/reference/api#response-and-error-codes ), you should try again later."
class Client:
    pass

print("Hello there!")
