from flask import Blueprint, jsonify, request

from backend_rest.awareness.app import db
from backend_rest.awareness.models import (
    User,
    TechnicalSupportTicket,
    TechnicalSupportChat,
)
from backend_rest.awareness.users.routes import token_required

technical_support_blueprint = Blueprint("technical_support", __name__)


@technical_support_blueprint.route(
    "/technical_support_tickets/new", methods=["POST", "GET"]
)
@token_required
def create_ticket():
    if request.method == "POST":
        ticket_json = request.get_json(force=True)

        token = request.headers["x-access-token"]
        user_id = User.decode_auth_token(token)

        title = ticket_json["title"]
        content = ticket_json["content"]
        is_resolved = False

        ticket = TechnicalSupportTicket(
            creator_id=user_id, title=title, content=content, is_resolved=is_resolved
        )

        db.session.add(ticket)
        db.session.commit()
        return jsonify(result="ticket added successfully", code=100)
    else:
        return jsonify(result="Unsupported request method", code=400)


@technical_support_blueprint.route(
    "/technical_support_tickets/<int:ticket_id>", methods=["GET"]
)
@token_required
def ticket(ticket_id):
    ticket = TechnicalSupportTicket.query.filter_by(id=ticket_id).first_or_404()
    chat_messages = TechnicalSupportChat.query.filter_by(ticket_id=ticket_id)
    messages_to_json = []
    for message in chat_messages:
        creator = User.query.get(message.user_id)
        msg = {"message": message.message, "creator": creator.nickname}
        messages_to_json.append(msg)
    return jsonify(
        title=ticket.title, content=ticket.content, messages=messages_to_json
    )


@technical_support_blueprint.route(
    "/technical_support_tickets/<int:ticket_id>", methods=["POST"]
)
@token_required
def make_message(ticket_id):
    ticket = TechnicalSupportTicket.query.filter_by(id=ticket_id).first_or_404()

    message_json = request.get_json(force=True)

    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    chat_message = TechnicalSupportChat(
        ticket_id=ticket.id, user_id=user_id, message=message_json["message"]
    )

    db.session.add(chat_message)
    db.session.commit()
    return jsonify(result="message sent successfully", code=100)


@technical_support_blueprint.route("/technical_support_tickets/users-tickets")
@token_required
def following_tickets():
    tickets = []
    token = request.headers["x-access-token"]
    user_id = User.decode_auth_token(token)

    following = TechnicalSupportTicket.query.filter_by(creator_id=user_id)
    sorted(following, key=lambda ticket: ticket.date)
    for ticket in following:
        tickets.append({"id": ticket.id, "title": ticket.title})
    return jsonify(tickets=tickets)
