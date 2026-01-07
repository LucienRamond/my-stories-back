from model.story import Story
from model.user import User
from server import db
from sqlalchemy.orm import contains_eager, joinedload

class StoriesService():
        def get_all_stories():

            try:
                  stories = Story.query.all()
                  users = User.query.all()
            except Exception as e:
                  return (f'{e}')

            return [{
                "id":story.id,
                "name":story.name,
                "story":story.story,
                "created_by":[{"name": user.username, "id": user.id} for user in users if user.id == story.created_by]
            } for story in stories]

        def create_story(story_data):
            story = Story(name=story_data["name"], story=story_data['story'], created_by=story_data['user_id'])
            db.session.add(story)
            db.session.commit()

            return (f'{story.id}')

        def update_story(story_id, story_data):
            story = Story.query.filter_by(id=story_id).first()

            if story_id != story_data['id']:
                return (f'Story can\'t be updated')

            story.name = story_data["name"]
            story.story = story_data["story"]

            db.session.commit()

            return (f'Story successfully updated')

        def delete_story(story_id):
            story = Story.query.filter_by(id=story_id).first()

            db.session.delete(story)
            db.session.commit()

            return (f'Story successfully deleted')