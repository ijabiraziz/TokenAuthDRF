add to installed_app:
    'rest_framework',
    'rest_framework.authtoken',


add to setting.py:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
    }


GO TO POSTMAN:
    - paste URI,
    - head over to header , in key enter "Autherization" While in value "token <your_token>",

Grab Token:
    - create superuser 
    - get token from token table