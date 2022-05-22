class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True
        #return self.is_sent

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


messages = []
while True:
    message = input().split(" ")
    if message[0] == "Stop":
        break
    current_sender = message[0]
    current_receiver = message[1]
    current_content = message[2]
    message = Email(current_sender, current_receiver, current_content)
    messages.append(message)

sent_indices = input().split(", ")
for index in range(len(messages)):
    for i in sent_indices:
        if index == int(i):
            messages[index].send()
    message_status = messages[index].get_info()

    print(message_status)