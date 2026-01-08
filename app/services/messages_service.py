from flask import make_response
from model.message import Message
import datetime
from server import db

class MessagesService():
    def get_messages_by_user_id(user_id):
        messages = Message.query.filter_by(sender_id=user_id)
        return messages

    def create_message(user_id, data):
        message = Message(sender_id=user_id, recipient_id=data['recipient_id'], message=data['message'], timestamp=datetime.datetime.now())
        db.session.add(message)
        db.session.commit()

        return make_response('Message successfully created')
    
    def get_messages(sender_id, data):
        messages_sender_to_recipient_query = MessagesService.get_messages_by_user_id(sender_id).filter_by(recipient_id=data['recipient_id']).all()
        messages_recipient_to_sender_query = MessagesService.get_messages_by_user_id(data['recipient_id']).filter_by(recipient_id=sender_id).all()

        messages_sender_to_recipient= [{
            'sender_id':message.sender_id, 
            'recipient_id':message.recipient_id, 
            'message':message.message, 
            'timestamp':message.timestamp } for message in messages_sender_to_recipient_query] 
        
        messages_recipient_to_sender = [{
            'sender_id':message.sender_id, 
            'recipient_id':message.recipient_id, 
            'message':message.message, 
            'timestamp':message.timestamp } for message in messages_recipient_to_sender_query]
        
        response = sorted(messages_sender_to_recipient + messages_recipient_to_sender, key=lambda x: x["timestamp"])
        
        return make_response(response)
