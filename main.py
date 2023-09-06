from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import  User, Tree, Bottle, Recommendation
from app.calculations import calculate_bottle_statistics, calculate_tree_statistics
import argparse
from sqlalchemy.ext.declarative import declarative_base


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
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

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

    # Calculate and display tree statistics
    user_id = 1
    tree_stats = calculate_tree_statistics(session, user_id)
    print("\nTree Statistics:")
    print(f"Trees Planted: {tree_stats['trees_planted']}")
    print(f"Trees Cut Down: {tree_stats['trees_cut_down']}")
    print(f"Net Effect: {tree_stats['net_effect']}")
    print(f"Message: {tree_stats['message']}")

    # Calculate and display bottle statistics
    bottle_stats = calculate_bottle_statistics(session, user_id)
    print("\nBottle Statistics:")
    print(f"Bottles Recycled: {bottle_stats['bottles_recycled']}")
    print(f"Bottles Disposed: {bottle_stats['bottles_disposed']}")
    print(f"Trash Effect: {bottle_stats['trash_effect']}")
    print(f"Message: {bottle_stats['message']}")

except Exception as e:
    print("Error:", str(e))
finally:
    session.close()