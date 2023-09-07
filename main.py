# from sqlalchemy import create_engine, exc
# from sqlalchemy.orm import sessionmaker
# from app.models import  User, Tree, Bottle, Recommendation
# from app.calculations import calculate_bottle_statistics, calculate_tree_statistics
# import argparse
# import random
# import click
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# engine = create_engine('sqlite:///user.db')

# connection= engine.connect()

# insert_sql_ignore = "INSERT OR IGNORE INTO users (username, age, email) VALUES (?, ?, ?)"
# data_ignore = [ 
#     ('Bilbo Boggins', 25, 'bilbo@hobbit.com')
# ]
# connection.execute(insert_sql_ignore, data_ignore)

# insert_sql_replace = "INSERT OR REPLACE INTO users (username, age, email) VALUES (?, ?, ?)"
# data_replace = [
#     ('Bilbo Boggins', 28, 'boggins@hobbit.com')
# ]
# connection.execute(insert_sql_replace, data_replace)

# connection.close()

# Base.metadata.create_all(engine)

# User.metadata.create_all(engine)
# Tree.metadata.create_all(engine)
# Bottle.metadata.create_all(engine)
# Recommendation.metadata.create_all(engine)



# def parse_args():
#     parser = argparse.ArgumentParser(description='Mother Gaia CLI')
#     parser.add_argument('--env', choices=['development','test'], default='development',
#                         help='Set the application environment mode (default:development)')
#     parser.add_argument('--user-id', type=int, help='User ID for statistics calculation')
#     return parser.parse_args()

# if __name__ == '__main__':
#     args = parse_args()
#     env_mode = args.env
#     user_id = args.user_id
#     print(f"Running in {env_mode} mode")

# if env_mode == 'development':
#     database_uri = 'sqlite:///user.db'
# elif env_mode == 'test':
#     database_uri = 'sqlite:///test_user.db'

# engine = create_engine(database_uri)
# Session = sessionmaker(bind=engine)
# session = Session()


# try:


#     users_data = [
#         {'username': 'Bilbo Boggins', 'age': 25, 'email' : 'bilbo@hobbit.com'},
#          {'username': 'Tony Rogers', 'age': 30, 'email' : 'rogers@hobbit.com'},
#           {'username': 'Eobard Allan', 'age': 19, 'email' : 'eobard@hobbit.com'},
#            {'username': 'Bruce Carpenter', 'age': 56, 'email' : 'carpenter@hobbit.com'},
#             {'username': 'GreenActivist11', 'age': 16, 'email' : 'activist@hobbit.com'},
#              {'username': 'GaiaGuardian', 'age': 67, 'email' : 'guardian@hobbit.com'},
#               {'username': 'NatureLover', 'age': 45, 'email' : 'nature@hobbit.com'},
#                {'username': 'Steve Jobless', 'age': 79, 'email' : 'steve@hobbit.com'},
#                 {'username': 'Slim Jim', 'age': 22, 'email' : 'slim@hobbit.com'},
#                  {'username': 'Patrick Tentacles', 'age': 52, 'email' : 'tentacles@hobbit.com'},
#                   {'username': 'Elon Tusk', 'age': 30, 'email' : 'tusk@hobbit.com'},
#                    {'username': 'Eric Myers', 'age': 14, 'email' : 'myers@hobbit.com'},
                  
#     ]


#     for data in users_data:
#         new_user = User(username=data['username'], age=data['age'], email=data['email'])
#         session.add(new_user)
#         session.commit()
    
    

#     for data in users_data:
#         existing_user = session.query(User).filter_by(username=data['username']).first()
#         if existing_user:
#         # If the user already exists, you can update their attributes
#             existing_user.age = data['age']
#             existing_user.email = data['email']
#         else:
#         # If the user doesn't exist, create a new one
#             new_user = User(username=data['username'], age=data['age'], email=data['email'])
#             session.add(new_user)

#     session.commit()

   
#     unique_ages = [random.randint(18, 60) for _ in range(10)]

# # Insert users with unique ages into the database
#     for age in unique_ages:
#        new_user = User(username='Bilbo Boggins', age=age, email='bilbo@hobbit.com')
#        session.add(new_user)
#        session.commit()

#     # Query Methods.
#     users = session.query(User).all()
#     print("All Users:")
#     for user in users:
#         print(f"User ID: {user.id}, Username: {user.username}, Age: {user.age},  Email: {user.email}")
    
    

#     # Insert Methods.
#     new_user = User(username='Fred Matthews', age= 20 ,email='matthews@hobbit.com')
#     session.add(new_user)
#     session.commit()
#     print("New user added with ID:", new_user.id)


#     #Update Records.
#     user_to_update = session.query(User).filter_by(username='Bilbo Boggins').first()
#     if user_to_update:
#      user_to_update.age = 25
#      user_to_update.email = 'boggins@hobbit.com'
#      session.commit()
#      print("User's age updated")


#     # Delete Records.
#     user_to_delete = session.query(User).filter_by(username='Bilbo Boggins').first()
#     if user_to_delete:
#         session.delete(user_to_delete)
#         session.commit()
#         print("User deleted!")

#     # Calculate and display tree statistics
#     trees_data = [
#      {'user_id':  4, 'action':'planted', 'trees_planted': 13,},
#      {'user_id':  2, 'action':'planted','trees_planted': 7},
#      {'user_id':  3, 'action':'cut down', 'trees_planted': -9},
#      {'user_id':  1, 'action':'planted', 'trees_planted': 21},
#      {'user_id':  1, 'action':'cut down', 'trees_planted':-1},
#      {'user_id':  5, 'action':'planted', 'trees_planted': 11},
#      {'user_id':  7, 'action':'planted', 'trees_planted': 34},
#      {'user_id':  4, 'action':'planted', 'trees_planted': 27},
#      {'user_id':  3, 'action':'cut down', 'trees_planted': -54},
#      {'user_id':  5, 'action':'cut down', 'trees_planted': -400},
#      {'user_id':  2, 'action':'planted', 'trees_planted': 640},
#      {'user_id':  4, 'action':'planted', 'trees_planted': 71},
#      {'user_id':  1, 'action':'cut down','trees_planted': -89},
#  ]

    
#     for data in trees_data:
#         user_id = data['user_id']
#         new_data = Tree(user_id=user_id, action=data['action'], trees_planted=data['trees_planted'])
#         session.add(new_data)
#         session.commit()
    
#     trees = session.query(Tree).all()
#     print("Tree Data:")
#     for tree in trees:
#         print(f"User ID: {tree.id}, Action: {tree.action}, Trees Planted: {tree.trees_planted} ")
    
#     user_id = 4
#     tree_stats = calculate_tree_statistics(session=session, user_id=user_id)
#     print("\nTree Statistics:")
#     print(f"Trees Planted: {tree_stats['trees_planted']}")
#     print(f"Trees Cut Down: {tree_stats['trees_cut_down']}")
#     print(f"Net Effect: {tree_stats['net_effect']}")
#     print(f"Message: {tree_stats['message']}")

#     # Calculate and display bottle statistics
#     bottle_data = [
#     {'user_id' : 1, 'action' :'recycled', 'bottles_recycled': 49},
#     {'user_id' : 2, 'action':'disposed', 'bottles_recycled': -32},
#    {'user_id' :  4, 'action':'recycled', 'bottles_recycled': 12},
#     {'user_id' : 4 , 'action':'recycled','bottles_recycled': 38},
#     {'user_id' : 3, 'action':'disposed', 'bottles_recycled': -9},
#     {'user_id' : 7, 'action':'recycled', 'bottles_recycled': 234},
#     {'user_id' : 5, 'action':'recycled', 'bottles_recycled': 50},
#     {'user_id' : 6, 'action':'recycled', 'bottles_recycled': 67},
#     {'user_id' : 5, 'action':'disposed', 'bottles_recycled': -73},
#     {'user_id' :8, 'action':'recycled', 'bottles_recycled': 24},
#    {'user_id' : 1, 'action':'disposed', 'bottles_recycled': -90},
#    {'user_id' : 3, 'action':'disposed','bottles_recycled': -101},
#     ]

#     for data in bottle_data:
#         user_id = data['user_id']
#         new_bottle_data = Bottle(user_id=user_id, action=data['action'], bottles_recycled=data['bottles_recycled'])
#         session.add(new_bottle_data)
#         session.commit()
    

#     user_id = data['user_id']
#     bottle_stats = calculate_bottle_statistics(session=session, user_id=user_id)
#     print("\nBottle Statistics:")
#     print(f"Bottles Recycled: {bottle_stats['bottles_recycled']}")
#     print(f"Bottles Disposed: {bottle_stats['bottles_disposed']}")
#     print(f"Trash Effect: {bottle_stats['trash_effect']}")
#     print(f"Message: {bottle_stats['message']}")

# except Exception as e:
#     session.rollback()
#     print("Error:", str(e))
# finally:
#     session.close()












import random
import click
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Tree, Bottle
from app.calculations import calculate_bottle_statistics, calculate_tree_statistics

engine = create_engine('sqlite:///user.db')
Session = sessionmaker(bind=engine)
session = Session()

def generate_random_username():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def generate_random_email():
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'hobbit.com', 'ballsdeep.com'])
    return f'{generate_random_username()}@{domain}'

@click.group()
@click.option('--env', type=click.Choice(['development', 'test']), default='development', help='Set the application environment mode (default: development)')
@click.option('--user-id', type=int, help='User ID for statistics calculation')
@click.pass_context
def cli(ctx, env, user_id):
    ctx.ensure_object(dict)
    ctx.obj['env'] = env
    ctx.obj['user_id'] = user_id


@cli.command()
@click.pass_context
def init_db(ctx):
    env_mode = ctx.obj['env']
    if env_mode == 'development':
        database_uri = 'sqlite:///user.db'
    elif env_mode == 'test':
        database_uri = 'sqlite:///test_user.db'
    
    engine = create_engine(database_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create and populate the User table
        users_data = [
            # {'username': 'Bilbo Boggins', 'age': 25, 'email': 'bilbo@hobbit.com'},
            # Add more user data here
        ]

        for data in users_data:
            existing_user = session.query(User).filter_by(username=data['username']).first()
            if existing_user:
                existing_user.age = data['age']
                existing_user.email = data['email']
            else:
                new_user = User(username=data['username'], age=data['age'], email=data['email'])
                session.add(new_user)

        session.commit()

        # Insert users with unique ages into the database
        unique_ages = [random.randint(18, 60) for _ in range(10)]

        used_usernames = set()
        used_emails = set()

        for age in unique_ages:
            while True:
                new_username = generate_random_username()
                if new_username not in used_usernames:
                    used_usernames.add(new_username)
                    break
            
            while True:
                new_email = generate_random_email()
                if new_email not in used_emails:
                    used_emails.add(new_email)
                    break

            new_user = User(username=new_username, age=age, email=new_email)
            session.add(new_user)
            session.commit()

        click.echo("Database initialized successfully!")

    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")
    finally:
        session.close()


@cli.command()
@click.pass_context
def calculate_statistics(ctx):
    user_id = ctx.obj['user_id']

    try:
        # Calculate and display tree statistics
        tree_stats = calculate_tree_statistics(session=session, user_id=user_id)
        click.echo("\nTree Statistics:")
        click.echo(f"Trees Planted: {tree_stats['trees_planted']}")
        click.echo(f"Trees Cut Down: {tree_stats['trees_cut_down']}")
        click.echo(f"Net Effect: {tree_stats['net_effect']}")
        click.echo(f"Message: {tree_stats['message']}")

        # Calculate and display bottle statistics
        bottle_stats = calculate_bottle_statistics(session=session, user_id=user_id)
        click.echo("\nBottle Statistics:")
        click.echo(f"Bottles Recycled: {bottle_stats['bottles_recycled']}")
        click.echo(f"Bottles Disposed: {bottle_stats['bottles_disposed']}")
        click.echo(f"Trash Effect: {bottle_stats['trash_effect']}")
        click.echo(f"Message: {bottle_stats['message']}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")
    finally:
        session.close()


if __name__ == '__main__':
    cli(obj={})
