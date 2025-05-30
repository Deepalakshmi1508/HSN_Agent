from agent.hsn_agent import HSNAgent

def main():
    agent = HSNAgent()
    while True:
        user_input = input("Enter HSN code or product description (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        response = agent.process_input(user_input)
        print(response)

if __name__ == "__main__":
    main()