import socket

"""""
    django automatically detects if app is in production or dev 
    by searching for a key word in hostname, add the key word here
"""
PRODUCTION = 'keywordtodetectprod' in socket.gethostname()
print(f'HOSTNAME = {socket.gethostname()}')

# is added to allowed hosts
PRODUCTION_IP = '123.456.789.101'

# only needed if reverse proxy is used
PROXY_IPS = ['in-case-of.proxy']

# gmail account for signup and pwd reset
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 123
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourMail@somemail.com'
EMAIL_HOST_PASSWORD = 'take23%§something§$§"%"long'

# this overrides the DEBUG var in settings.py for debugging set to True
DEBUG_PROD = False