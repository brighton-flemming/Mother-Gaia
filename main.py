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
@click.option('--user-id', prompt='Enter user ID', type=int, help='User ID statistics calculation')
@click.pass_context
def calculate_statistics(ctx, user_id):
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

@cli.command()
@click.option('--username', prompt='Enter username', help='Username of the user to add')
@click.option('--age', prompt='Enter age', help='Age of the user to add')
@click.option('--email', prompt='Enter email', help='Email of the user to add')
@click.pass_context
def add_user(ctx, username, age, email):
    try:
        new_user = User(username=username, age=age, email=email)
        session.add(new_user)
        session.commit()
        click.echo(f"User '{username}' added successfully!")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--username', prompt='Enter username', help='Username of the user to delete')
@click.pass_context
def delete_user(ctx, username):
    try:
        user_to_delete = session.query(User).filter_by(username=username).first()
        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
            click.echo(f"User '{username}' deleted successfully!")
        else:
            click.echo(f"User 'username' not found.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--username', prompt='Enter username', help='Username of the user to update')
@click.option('--new-age', prompt='Enter new age', type=int, help='New age for the user')
@click.option('--new-email', prompt='Enter new email', help='New email for the user')
@click.pass_context
def update_user(ctx, username, new_age, new_email):
    try:
        user_to_update = session.query(User).filter_by(username=username).first()
        if user_to_update:
            user_to_update.age = new_age
            user_to_update.email = new_email
            session.commit()
            click.echo(f"User '{username}' updated successfully!")
        else:
            click.echo(f"User '{username}' not found.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")
    finally:
        session.close()


@cli.command()
@click.option('--user-id', prompt='Enter user ID', type=int, help='User ID for the bottle action')
@click.option('--action', prompt='Enter action', type=click.Choice(['recycled', 'disposed']), help='Action performed with the botttles')
@click.option('--bottles-recycled', prompt='Enter number of bottles recycled', type=int, help='Number of bottles recycled')
@click.option('--bottles-disposed', prompt='Enter number of bottles disposed', type=int, help='Number of bottles disposed')
@click.pass_context
def add_bottle(ctx, user_id, action, bottles_recycled, bottles_disposed):
    try:
        if action == 'recycled':
            trash_effect = bottles_recycled - bottles_disposed
        else:
            trash_effect = bottles_disposed - bottles_recycled
        
        new_bottle_data = Bottle(user_id=user_id, action=action, bottles_recycled=bottles_recycled, bottles_disposed=bottles_disposed, trash_effect=trash_effect)
        session.add(new_bottle_data)
        session.commit()
        click.echo("Bottle instance added successfully!")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {str(e)}")
    finally:
        session.close()


@cli.command()
@click.option('--user-id', prompt='Enter user ID', type=int, help='User ID for the tree action')
@click.option('--action', prompt='Enter action', type=click.Choice(['planted', 'cut down']), help='Action performed with the tree')
@click.option('--trees', prompt='Enter number of trees', type=int, help='Number of trees involved in the action')
@click.pass_context
def add_tree(ctx, user_id, action, trees):
    try:
        if action == 'planted':
            trees_planted = trees
            trees_cut_down = 0
        elif action == 'cut down':
            trees_planted = 0
            trees_cut_down = trees

        net_effect = trees_planted - trees_cut_down

        new_tree_data = Tree(
            user_id=user_id,
            action=action,
            trees_planted=trees_planted,
            trees_cut_down=trees_cut_down,
            net_effect=net_effect
        )

        session.add(new_tree_data)
        session.commit()
        click.echo("Tree instance added successfully!")
    except Exception as e:
        session.rollback()
        click.echo(f"Echo: {str(e)}")
    finally:
        session.close()

if __name__ == '__main__':
    cli(obj={})
