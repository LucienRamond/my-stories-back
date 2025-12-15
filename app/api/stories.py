from flask import Blueprint, request
from services.stories_service import StoriesService

stories_route = Blueprint("stories_route", __name__)

@stories_route.route('/stories', methods=['GET'])
def get_stories():
    return StoriesService.get_all_stories()

@stories_route.route('/stories/create', methods=['POST'])
def create():
    data = request.get_json()
    return StoriesService.create_story(data)


@stories_route.route('/stories/delete/<int:story_id>', methods=['DELETE'])
def delete(story_id):
    return StoriesService.delete_story(story_id)