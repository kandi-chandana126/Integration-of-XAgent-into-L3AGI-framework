from xagent import XAgent

class ConversationalAgent:
    def __init__(self):
        self.agent = XAgent()

    def converse(self, input_text):
        return self.agent.get_response(input_text)
