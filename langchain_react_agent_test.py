from langchain import ReactAgent

agent = ReactAgent()

def test_conversation():
    input_text = "Hello, how are you?"
    response = agent.get_response(input_text)
    print(response)

if __name__ == "__main__":
    test_conversation()
