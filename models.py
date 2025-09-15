import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Topic(db.Model):
    __tablename__ = "topics"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    parent_topic_id = db.Column(UUID(as_uuid=True), db.ForeignKey("topics.id"), nullable=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "parentTopicID": str(self.parent_topic_id) if self.parent_topic_id else None
        }

class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    difficulty = db.Column(db.String, default="unknown")
    topic_id = db.Column(UUID(as_uuid=True), db.ForeignKey("topics.id"), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "difficulty": self.difficulty,
            "topicId": str(self.topic_id)
        }


# class Skill(db.Model):
#     __tablename__ = "skills"
#     id = db.Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
#     name = db.Column(db.String, nullable=False)
#     topic_id = db.Column(
#         UUID(as_uuid=False), 
#         db.ForeignKey("topics.id", ondelete="CASCADE"), 
#         nullable=False
#         )
#     difficulty = db.Column(db.String, nullable=False)
#     created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "topicID": self.topic_id,
#             "difficulty": self.difficulty,
#             "createdAt": self.created_at
#         }
    