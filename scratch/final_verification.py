import json
from analytics_system.chatbot import ValorantChatbot

def final_verify():
    print("Initializing Chatbot...")
    bot = ValorantChatbot()
    print("Chatbot Initialized.")
    
    query = "Predict a match on Bind where Team A has TenZ and Zellsis, and Team B has Demon1 and Ethan."
    print(f"\nTesting Query: {query}")
    
    import time
    start = time.time()
    res = bot.handle_query(query)
    end = time.time()
    
    print(f"Time taken: {end - start:.2f}s")
    print(f"Response: {res['response']}")
    if res['data'] and res['data']['type'] == 'match_prediction':
        print("SUCCESS: Match prediction structured data generated.")
        # print(json.dumps(res['data']['analysis']['team_a']['players'], indent=2))
        players_a = [p['name'] for p in res['data']['analysis']['team_a']['players']]
        players_b = [p['name'] for p in res['data']['analysis']['team_b']['players']]
        print(f"Team A recognized: {players_a}")
        print(f"Team B recognized: {players_b}")
    else:
        print("FAILURE: Specialized match prediction data NOT found.")

if __name__ == "__main__":
    final_verify()
