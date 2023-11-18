import psycopg2

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

# Create a cursor
cursor = connection.cursor()

# Execute SQL queries
# ...

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
