from app.main.models.BaseModel import db
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey


class Game(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"), )
    game_id = db.Column(db.String(12), index=True, unique=True)
    owner = db.Column(ForeignKey('user.id', ondelete='CASCADE'), index=True)
    display_name = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.username)
