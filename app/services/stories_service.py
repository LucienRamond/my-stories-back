from model.story import Story
from server import db

class StoriesService():
        def get_all_stories():

            try:
                  stories = (Story.query.all())
            except Exception as e:
                  return (f'{e}')


            return [{
                "id":story.id,
                "name":story.name,
                "story":story.story,
            } for story in stories]

        def create_story(story_data):
            story = Story(name=story_data["name"], story=story_data['story'])
            db.session.add(story)
            db.session.commit()

            return (f'{story.id}')

        def delete_story(story_id):
            story = Story.query.filter_by(id=story_id).first()

            db.session.delete(story)
            db.session.commit()

            return (f'Story successfully deleted')