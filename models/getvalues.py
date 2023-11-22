from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model import UserAccount

def select_user_details(engine_url):
    engine = create_engine(engine_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Define the columns you want to select
        user_name_column = UserAccount.user_name
        user_email_column = UserAccount.user_email
        year_of_birth_column = UserAccount.year_of_birth

        # Build the select query
        query = select(user_name_column, user_email_column, year_of_birth_column)

        # Execute the query and fetch results
        result = session.execute(query).fetchall()

        # Print the selected details
        for row in result:
            print(f"User Name: {row[0]}, User Email: {row[1]}, Year of Birth: {row[2]}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    # Replace 'your_database_url' with the actual URL of your database
    database_url = 'postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase'
    select_user_details(database_url)
