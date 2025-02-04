from flask import g
from flask import Blueprint
from flask import Response
from flask import request

import math

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
    display_name = fields.String()
    value = fields.Number()
    date = fields.DateTime()


class ScoreSchema(Schema):
    display_name = fields.String()
    value = fields.Number()
    date = fields.DateTime()


class LeaderBoardSchema(Schema):
    position = fields.Number()
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
        #player_score = request.args.get('score')
        player_score = None
        limit = request.args.get('limit', 0)
        offset = request.args.get('offset', 0)
        scores, err = get_scores_for_game(game_id)

        if err:
            return {'error': f'Could not find game with game_id {game_id}'}, 400

        filtered_sores = []
        player_pos = 0
        if player_score:
            for i in range(0, len(scores)):
                player_pos = i
                if player_score > scores[i]:
                    break

        if limit:
            #start_index = max(len(scores) - player_pos - (limit / 2), 0)
            #end_index = player_pos + (limit / 2)
            filtered_sores = scores[offset: offset + int(limit)]
        else:
            filtered_sores = scores

        return LeaderBoardSchema().dump({
            'scores': filtered_sores,
            'position': (player_pos + 1),
            'count': len(filtered_sores)
        })

    def post(self, game_id):
        payload = request.json
        #validated_input = AddScoreSchema().load(payload) #TODO
        score, err = create_score(game_id, payload)
        if err is not None:
            return {'error': f'Could not find game with game_id {game_id}'}, 400
        return {'message': 'score saved'}, 200


games_api.add_resource(Games, '/games')
games_api.add_resource(GameScores, '/scores/<string:game_id>')