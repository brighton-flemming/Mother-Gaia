
from app.models import User, Tree, Bottle
from sqlalchemy.orm import Session
from sqlalchemy import func

def calculate_tree_statistics(session:Session, user_id: int) -> dict:

    trees_planted = session.query(func.sum(Tree.trees_planted)).filter_by(user_id=user_id, action='planted').scalar() or 0
    trees_cut_down = session.query(func.sum(Tree.trees_cut_down)).filter_by(user_id=user_id, action='cut down').scalar() or 0
    net_effect = trees_planted - trees_cut_down

    if net_effect > 0:
        message = "Good job making the world a little greener (*o*)!"
    elif net_effect < 0:
        message = "The same environment that you are harming is the same one that your kids will grow up in (*_*)!"
    else:
        message = "Hello there,NPC. Please add a bit of flair in your life by planting more trees(!o!)! "


    trees_statistics = {
        'trees_planted': trees_planted,
        'trees_cut_down': trees_cut_down,
        'net_effect': net_effect,
        'message': message
    }

    return trees_statistics
    
    

def calculate_bottle_statistics(session:Session, user_id: int) -> dict:

    bottles_recycled = session.query(func.sum(Bottle.bottles_recycled)).filter_by(user_id=user_id, action='recycled').scalar() or 0
    bottles_disposed = session.query(func.sum(Bottle.bottles_disposed)).filter_by(user_id=user_id, action='disposed').scalar() or 0
    trash_effect = bottles_recycled - bottles_disposed

    if trash_effect > 0 :
        message = "Fine job,mate! Keep recycling and reducing waste (^ _ ^)!"
    elif trash_effect < 0 :
        message = "Please don't think like the bottles you throw away aimlessly. Be better, be green. (# w #)"
    else:
        message = "Your recycling efforts are neutral. Do something with a bottle. Anything (~ _ ~)!"
    

    bottles_statistics = {
        'bottles_recycled': bottles_recycled ,
        'bottles_disposed': bottles_disposed,
        'trash_effect': trash_effect,
        'message': message
    }

    return bottles_statistics