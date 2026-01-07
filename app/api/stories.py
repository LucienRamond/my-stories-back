from flask import Blueprint, request
from services.stories_service import StoriesService
from utils.JwtToken import token_required

stories_route = Blueprint("stories_route", __name__)

@stories_route.route('/stories', methods=['GET'])
def get_stories():
    return StoriesService.get_all_stories()

@stories_route.route('/stories/create', methods=['POST'])
@token_required
def create():
    data = request.get_json()
    return StoriesService.create_story(data)

@stories_route.route('/stories/update/<int:story_id>', methods=['PATCH'])
@token_required
def update(story_id):
    data = request.get_json()
    return StoriesService.update_story(story_id, data)

@stories_route.route('/stories/delete/<int:story_id>', methods=['DELETE'])
@token_required
def delete(story_id):
    return StoriesService.delete_story(story_id)