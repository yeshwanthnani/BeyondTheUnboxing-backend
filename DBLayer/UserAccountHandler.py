from models.model import UserAccount, db
from sqlalchemy.exc import IntegrityError
from models.exceptions import UserAlreadyExists, UserDoesNotExist
from flask import jsonify


class UserAccountHandler:

    def __init__(self):
        return

    @staticmethod
    def create_user(user_name, user_email, password, year_of_birth):
        try:
            # Create a new user instance
            new_user = UserAccount(
                user_name=user_name,
                user_email=user_email,
                password=password,
                year_of_birth=year_of_birth
            )

            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except IntegrityError as e:
            raise UserAlreadyExists()

    @staticmethod
    def delete_user(user_ID):
        # Find the user by ID
        user_to_delete = UserAccount.query.get(user_ID)

        # Check if the user exists
        if user_to_delete:
            # Delete the user from the database
            db.session.delete(user_to_delete)
            db.session.commit()
            return True
        else:
            raise UserDoesNotExist()



    @staticmethod
    def get_user_details(user_ID):
        user = UserAccount.query.get(user_ID)

        if user:
            response = {
                'user_ID': user.user_ID,
                'user_name': user.user_name,
                'user_email': user.user_email,
                'year_of_birth': user.year_of_birth
            }
            return response
        elif user is None:
            raise UserDoesNotExist()


