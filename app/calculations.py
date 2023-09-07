
from app.models import User, Tree, Bottle
from sqlalchemy.orm import Session

def calculate_tree_statistics(session:Session, user_id: int) -> dict:

    trees_planted = session.query(Tree).filter_by(user_id=user_id, action='planted').count()
    trees_cut_down = session.query(Tree).filter_by(user_id=user_id, action='cut down').count()
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

    bottles_recycled = session.query(Bottle).filter_by(user_id=user_id, action='recycled').count()
    bottles_disposed = session.query(Bottle).filter_by(user_id=user_id, action='disposed').count()
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