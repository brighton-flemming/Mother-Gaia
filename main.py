from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Tree, Bottle, Recommendation
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

    users = session.query(User).all()
    print("All Userd:")
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")

except Exception as e:
    print("Error:", str(e))
finally:
    session.close()