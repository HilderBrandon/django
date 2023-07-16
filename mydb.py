from MySQLdb import MySQLError
import MySQLdb
from django.conf import settings

# Obtener los datos de configuración de la base de datos
database_config = settings.DATABASES['default']

# Establecer la conexión
try:
    connection = MySQLdb.connector.connect(
        user=database_config['USER'],
        password=database_config['PASSWORD'],
        host=database_config['HOST'],
        database=database_config['NAME'],
        port=database_config['PORT']
    )
    print("Conexión exitosa a la base de datos")
except MySQLError.connector.Error as error:
    print("Error al conectarse a la base de datos: {}".format(error))
