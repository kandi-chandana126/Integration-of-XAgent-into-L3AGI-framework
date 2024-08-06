from xagent import XAgent

class DialogueAgentWithTools:
    def __init__(self):
        self.agent = XAgent()

    def handle_dialogue(self, input_text):
        return self.agent.get_response(input_text)
