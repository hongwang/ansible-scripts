#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 5000
SUPERSET_WORKERS = 4

SUPERSET_WEBSERVER_PORT = 30002
SUPERSET_WEBSERVER_TIMEOUT = 600
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = 'sdjklasdjkalsjdfasdfasdfasdfasdf'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'mysql://hive:HCDhcd123@uat-mysql-01:3306/superset'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''


CACHE_CONFIG = {'CACHE_TYPE': 'simple'}
TABLE_NAMES_CACHE_CONFIG = {'CACHE_TYPE': 'simple'}


SQLLAB_TIMEOUT = 600
