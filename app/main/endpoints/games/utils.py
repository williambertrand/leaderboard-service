from app.main.models import (
    Game,
    User,
    Score
)

from app import db
from uuid import uuid4


def get_game_id():
    exists = True
    while exists:
        x = uuid4()
        new_id = str(x)[:8]
        exists = Game.query.filter(Game.game_id == new_id).one_or_none() is not None
    return new_id


def create_new_game(game_data):
    game_id = get_game_id()
    game = Game(
        owner=game_data['owner_id'],
        game_id=game_id,
        display_name=game_data['display_name']
    )
    db.session.add(game)
    db.session.commit()


# TODO: Non-desc order may be needed
def get_scores_for_game(game_id):
    scores = Score.query.filter(Score.game == game_id).order_by(Score.value.desc()).all()
    return scores


def create_score(score_data):
    game_short_id = score_data['game_id']
    game_ref = Game.query.filter(Game.game_id == game_short_id).one_or_none()
    new_score = Score(
        game=game_ref.id,
        display_name=score_data['display_name'],
        value=score_data['value']
    )

    db.session.add(new_score)
    db.session.commit()
