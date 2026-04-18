
from analytics_system.chatbot import ValorantChatbot
import spacy

try:
    bot = ValorantChatbot()
    print("Chatbot initialized successfully!")
    res = bot.handle_query("predict a match between TenZ and Demon1 on Bind")
    print("Query handled successfully!")
    print(res)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
