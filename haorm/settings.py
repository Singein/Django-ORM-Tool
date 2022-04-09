import json
import os
import uuid

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(uuid.uuid1())

with open(os.environ['DOTLIB_DBCONFIG_PATH'], encoding='utf-8') as f:
    configs = f.read()

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASE_ROUTERS = ['haorm.router.DataBaseRouter']
DATABASES = json.loads(configs)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'
