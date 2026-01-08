from flask import Blueprint, request
from services.messages_service import MessagesService
from utils.JwtToken import token_required

messages_route = Blueprint("messages_route", __name__)

@messages_route.route('/messages/<int:sender_id>', methods=['POST'])
def get_messages(sender_id):
    recipient_id = request.get_json()
    return MessagesService.get_messages(sender_id, recipient_id)

@messages_route.route('/messages/create/<int:sender_id>', methods=['POST'])
def create_message(sender_id):
    data = request.get_json()
    return MessagesService.create_message(sender_id, data)