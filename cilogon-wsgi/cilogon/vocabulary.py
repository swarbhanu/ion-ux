from rdflib import URIRef
import hashlib
import random

#########################################
# Namespaces
#########################################
CILOGON = URIRef('ncsa:cilogon.org,2010:/1.0/')
CILOGON_URI_SCHEME = 'ncsa'
CILOGON_URI_SCHEME_SPECIFIC_PART = 'cilogon.org,2010'
CONFIGURATION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/')
CONFIG_ROOT_NAME = 'ncsa:cilogon.org,2010:/1.0/configuration/rootname'
DATABASE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/database/')
FILE_STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/fileStore/')
MEMORY_STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/memory/')
MYSQL_STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/mysqlStore/')
POSTGRES_STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/postgreStore/')
DJANGO_STORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/djangoStore/')
SQL_COLUMN_NS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/')
SQL_CONNECTION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/')
SQL_SEQUENCE_NS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlSequence/')
SQL_STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/')
SQL_TABLE_NS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlTable/')
SQL_TRANSACTION_NS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/')
SSL = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/')
STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/store/')
VERSION = URIRef('1.0')


#########################################
# Vocabulary
#########################################
CONNECTION_ADMIN_DRIVER = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/adminJdbcDriver')
CONNECTION_ADMIN_HOST = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/adminHost')
CONNECTION_ADMIN_PASSWORD = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/adminPassword')
CONNECTION_ADMIN_PORT = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/adminPort')
CONNECTION_ADMIN_USERNAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/adminUsername')
CONNECTION_DRIVER = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/jdbcDriver')
CONNECTION_HOST = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/host')
CONNECTION_PASSWORD = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/password')
CONNECTION_PORT = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/port')
CONNECTION_USERNAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/username')
FILE_DATA_PATH = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/fileStore/dataPath')
FILE_INDEX_PATH = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/fileStore/lookupPath')
FILE_STORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/fileStore/')
HAS_ADMIN_CONNECTION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasAdminConnection')
HAS_CONNECTION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasConnection')
HAS_DATABASE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasDatabase')
HAS_PORTAL_PARAMETERS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal/hasPortalParameters')
HAS_SEQUENCE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasSequence')
HAS_SSL_CONFIGURATION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasSSL')
HAS_STORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasStore')
HAS_TABLE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasTable')
HAS_TRANSACTION_TABLE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasTransactionTable')
MEMORY_STORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/memory/')
MYSQL_STORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/mysqlStore/')
PORTAL_CALLBACK_URI = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#callbackUri')
PORTAL_CERT_REQ_CONFIGURATION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#certReqConfig')
PORTAL_FAILURE_URI = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#failureUri')
PORTAL_HOST_CERT = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#hostCred')
PORTAL_HOST_KEY = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#hostKey')
PORTAL_NAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#portalName')
PORTAL_PARAMETERS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal/')
PORTAL_SUCCESS_URI = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#successUri')
PORTAL_TEMPORARY_DIRECTORY = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/portal#tempDirectory')
POSTGRES_STORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/postgreStore/')
ROOT_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/root/')
SQL_ADMIN_CONNECTION_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/admin/')
SQL_COLUMN_BOOLEAN_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/integer')
SQL_COLUMN_DATA_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/columnType')
SQL_COLUMN_DATE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/date')
SQL_COLUMN_INTEGER_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/boolean')
SQL_COLUMN_NAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/name')
SQL_COLUMN_STRING_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/string')
SQL_COLUMN_TIMESTAMPE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/timestamp')
SQL_COLUMN_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/column')
SQL_COLUMN_UID = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/columnUID')
SQL_CONNECTION_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/connection/')
SQL_DATABASE_NAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/database/databaseName')
SQL_DATABASE_SCHEMA = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/database/schema')
SQL_DATABASE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/database/database')
SQL_HAS_COLUMN = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/hasColumn')
SQL_SEQUENCE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlSequence/sequence')
SQL_SEQUENCE_NAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlSequence/uid_seq')
SQL_STORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlStore/')
SQL_TABLE_NAME = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlTable/name')
SQL_TABLE_PREFIX = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlTable/prefix')
SQL_TABLE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlTable/table')
SSL_CONFIGURATIION = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/')
SSL_HOST_CERT = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/hostCred')
SSL_HOST_KEY = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/hostKey')
SSL_KEYSTORE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/keyStore')
SSL_KEYSTORE_PASSWORD = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/keyStorePassword')
SSL_KEYSTORE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/keyStoreType')
SSL_KEY_MANAGER_FACTORY = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/keyManagerFactory')
SSL_TRUST_ROOT_PATH = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/ssl/trustRootPath')
STORE_CLASS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/store/storeClass')
TRANSACTION_TABLE_COLUMN_ACCESS_TOKEN = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/accessToken')
TRANSACTION_TABLE_COLUMN_ACCESS_TOKEN_SS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/accessTokenSS')
TRANSACTION_TABLE_COLUMN_CERTIFICATE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/certificate')
TRANSACTION_TABLE_COLUMN_COMPLETE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/complete')
TRANSACTION_TABLE_COLUMN_IDENTIFIER = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/transactionUID')
TRANSACTION_TABLE_COLUMN_PRIVATE_KEY = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/privateKey')
TRANSACTION_TABLE_COLUMN_REDIRECT_URI = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/redirectUri')
TRANSACTION_TABLE_COLUMN_TEMP_CRED = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/tempCred')
TRANSACTION_TABLE_COLUMN_TEMP_CRED_SS = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/tempCredSS')
TRANSACTION_TABLE_COLUMN_VERIFIER = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlColumn/transaction/verifier')
TRANSACTION_TABLE_TYPE = URIRef('ncsa:cilogon.org,2010:/1.0/configuration/sqlTable/transaction/')

# create a new uri ref.
def uriRef():
    seed= ''.join([str(random.randint(0, 9)) for i in range(64)]) # seed it
    return URIRef(CILOGON_URI_SCHEME + ":" + CILOGON_URI_SCHEME_SPECIFIC_PART + ":" + hashlib.sha1(seed).hexdigest())
