import datetime
# from accounts.utils import jwt_get_user_id_from_payload_handler

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication', # OAuth, JWT, OAuth2
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ],

}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':    
    'accounts.api.utils.jwt_get_user_id_from_payload_handler',
    #'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',   
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer', 

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}