import jwt
import logging
from functools import wraps
from flask import request, g
from dbmonit.models import User, Client
from dynaconf import settings

logger = logging.getLogger(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        req_token = request.headers.get("Authorization", "")

        if "Bearer " not in req_token:
            return (
                {"error": "Bearer is not in header"},
                401,
            )

        _, token = req_token.split(" ")

        try:
            data = jwt.decode(token, settings.JWT_SECRET_KEY)
            if "user_data" in data:
                user = User.query.filter_by(**data.get("user_data")).first()
                g.user = user

        except jwt.ExpiredSignatureError:
            # valid token, but expired
            return {"error": "Token expired"}
        except jwt.InvalidTokenError:
            # invalid token
            return (
                {"error": "Invalid Token Error"},
                401,
            )
        except Exception:
            return (
                {"error": "error"},
                401,
            )

        return f(*args, **kwargs)

    return decorated_function


def client_secret_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_secret = request.headers.get('CSecret', '')
        client = Client.query.filter_by(client_secret=client_secret).first()

        if client:
            return f(*args, **kwargs)
        
        return {'error': 'Invalid Client Secret Error'}, 401
    
    return decorated_function