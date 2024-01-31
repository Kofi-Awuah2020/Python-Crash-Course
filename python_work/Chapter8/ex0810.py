def send_messages(text_messages, sent_messages):
    while text_messages:
        current_message = text_messages.pop()
        print(f"\n{current_message}")
        sent_messages.append(current_message)

short_texts =['lmao', 'omg', 'wllnh', 'lwkmd']
sent_messages = []
send_messages(short_texts, sent_messages)
print(short_texts)
print(sent_messages)