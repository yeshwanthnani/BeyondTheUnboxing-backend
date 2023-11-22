import psycopg2
from sqlalchemy import create_engine

# Replace these values with your database information
db_params = {
    'dbname': 'MyDataBase',
    'user': 'postgres',
    'password': 'Nani8901',
    'host': 'database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com',
    'port': '5432',
}

# Establish a connection
connection = psycopg2.connect(**db_params)

engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}")

# Create a cursor
cursor = connection.cursor()

# Execute SQL queries
# ...

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
