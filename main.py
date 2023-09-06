from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import  User, Tree, Bottle, Recommendation
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Mother Gaia CLI')
    parser.add_argument('--env', choices=['development','test'], default='development',
                        help='Set the application environment mode (default:development)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    env_mode = args.env
    print(f"Running in {env_mode} mode")

if env_mode == 'development':
    database_uri = 'sqlite:///user.db'
elif env_mode == 'test':
    database_uri = 'sqlite:///test_user.db'

engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session = Session()

try:
    
    # Query Methods.
    users = session.query(User).all()
    print("All Userd:")
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")

    # Insert Methods.
    new_user = User(username='new_user', email='new_user@example.com')
    session.add(new_user)
    session.commit()
    print("New user added with ID:", new_user.id)

    # Update Records.
    user_to_update = session.query(User).filter_by(username='new_user').first()
    if user_to_update:
        user_to_update.email = 'updated_email@example.com'
        session.commit()
        print("User's email updated")

    # Delete Records.
    user_to_delete = session.query(User).filter_by(username='new_user').first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print("User deleted!")

except Exception as e:
    print("Error:", str(e))
finally:
    session.close()