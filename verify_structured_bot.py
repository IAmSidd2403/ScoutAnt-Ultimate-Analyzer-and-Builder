import json
from analytics_system.chatbot import ValorantChatbot

def test_chatbot():
    bot = ValorantChatbot()
    
    queries = [
        "What is the best agent for TenZ on Bind?",
        "How do I counter Jett on Haven?",
        "Predict a match between TenZ, Zellsis vs Demon1, Ethan on Pearl",
    ]
    
    for q in queries:
        print(f"\nQuery: {q}")
        res = bot.handle_query(q)
        print(f"Response: {res['response']}")
        print(f"Data type: {res['data']['type'] if res['data'] else 'None'}")
        if res['data']:
            print("Structured data generated successfully.")

if __name__ == "__main__":
    test_chatbot()
