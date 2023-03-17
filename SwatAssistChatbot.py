from SwatAssistModel import find_most_similar_question

# Test the chatbot
while True:
    print(".........................................")
    print("How can Vroozi assist you ?")
    question = input("Please feel free to ask any questions you may have : ")
    if question.lower() == 'exit':
        break
    if len(question.split()) < 3:
        print("Provided information is too short to fully understand your query.\n Please feel free to provide more "
              "details or ask a more specific question,\n and I will do my best to provide a helpful response.\n "
              "Alternatively,you can provide some context or background information to help me better understand "
              "your question.\n Thank you! ")
        continue
    else:
        answer = find_most_similar_question(question)
        print(answer)
