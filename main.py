from ticket_comments import getTicketComments
from SwatAssistModel import find_most_similar_question
from zendesk_comment_posting import post_answer


def postReplyToZendesk():
    ticketId = "163831";
    ticket_form_id = "12477608020500";
    comments = getTicketComments(ticketId);

    print(comments[0]);

    answer = find_most_similar_question(comments[0]);
    post_answer(answer, ticket_form_id);
    print(answer);