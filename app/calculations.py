
from app.models import User, Tree
from sqlalchemy.orm import Session

def calculate_tree_statistics(session:Session, user_id: int) -> dict:

    trees_planted = session.query(Tree).filter_by(user_id=user_id, action='planted').count()
    trees_cut_down = session.query(Tree).filter_by(user_id=user_id, action='cut down').count()
    net_effect = trees_planted - trees_cut_down