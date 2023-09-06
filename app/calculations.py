
from app.models import User, Tree, Bottle
from sqlalchemy.orm import Session

def calculate_tree_statistics(session:Session, user_id: int) -> dict:

    trees_planted = session.query(Tree).filter_by(user_id=user_id, action='planted').count()
    trees_cut_down = session.query(Tree).filter_by(user_id=user_id, action='cut down').count()
    net_effect = trees_planted - trees_cut_down
    trees_statistics = {
        'trees_planted': trees_planted,
        'trees_cut_down': trees_cut_down,
        'net_effect': net_effect
    }

    return trees_statistics

def calculate_bottle_statistics(session:Session, user_id: int) -> dict:

    bottles_recycled = session.query(Bottle).filter_by(user_id=user_id, action='recycled').count()
    bottles_disposed = session.query(Bottle).filter_by(user_id=user_id, action='disposed').count()
    trash_effect = bottles_recycled - bottles_disposed
    bottles_statistics = {
        'bottles_recycled': bottles_recycled ,
        'bottles_disposed': bottles_disposed,
        'trash_effect': trash_effect
    }

    return bottles_statistics