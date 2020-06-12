from flask import g
from flask import Blueprint
from flask import Response
from flask import request

from marshmallow import Schema
from marshmallow import fields

from flask_restful import Api
from flask_restful import Resource

from .utils import (
    create_new_game,
    get_scores_for_game,
    create_score
)


class GameSchema(Schema):
    display_name = fields.String(required=True)
    game_id = fields.String(required=False)
    owner_id = fields.String(required=True)


class AddScoreSchema(Schema):
    game_id = fields.String(required=True)
    display_name = fields.String()
    value = fields.Number()
    date = fields.DateTime()

class ScoreSchema(Schema):
    display_name = fields.String()
    value = fields.Number()
    date = fields.DateTime()


class LeaderBoardSchema(Schema):
    scores = fields.Nested(ScoreSchema, many=True)
    count = fields.Number()


games_bp = Blueprint('games', __name__)
games_api = Api(games_bp)


class Games(Resource):
    def post(self):
        payload = request.json
        validated_input = GameSchema().load(payload)
        new_game = create_new_game(validated_input)
        return GameSchema().dump(new_game)


class GameScores(Resource):
    def get(self, game_id):
        scores = get_scores_for_game(game_id)

        return LeaderBoardSchema().dump({
            'scores': scores,
            'count': len(scores)
        })


class Score(Resource):
    def post(self):
        payload = request.json
        validated_input = AddScoreSchema().load(payload)
        score = create_score(validated_input)

        return {'message': 'score saved'}, 200


games_api.add_resource(Games, '/games')
games_api.add_resource(Score, '/scores')
games_api.add_resource(GameScores, '/scores/<string:game_id>')