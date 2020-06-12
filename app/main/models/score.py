from app.main.models.BaseModel import db
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
from sqlalchemy import func


class Score(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"), )
    game = db.Column(ForeignKey('game.id', ondelete='CASCADE'), index=True)

    display_name = db.Column(db.String(120))
    value = db.Column(db.Numeric())

    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return '<User {}>'.format(self.username)
