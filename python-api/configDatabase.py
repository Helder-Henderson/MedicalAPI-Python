import dotenv as _env

_ENV = _env.dotenv_values()
SERVER = _ENV.get('SERVER')
DATABASE =_ENV.get('DATABASE')
USERNAME = _ENV.get('UID')
PASSWORD = _ENV.get('PASSWORD')
DRIVER = _ENV.get('DRIVER')

CONNECTION_STRING = 'DRIVER='+DRIVER+';SERVER=tcp:'+SERVER+';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
