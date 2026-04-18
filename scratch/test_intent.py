from analytics_system.chatbot import ValorantChatbot
import spacy

# Mock the chatbot but ignore the spacy load if possible or just use a test instance
# Note: In a real environment we might need to install spacy model first
# but here we assume it's installed.

bot = ValorantChatbot()
test_input = "Team A is yay on Chamber, crashies on Sova, Victor on KAY/O, FNS on Omen, and Marved on Astra Team B features Derke on Jett, Leo on Fade, Alfajer on Killjoy, Boaster on Omen, and Chronicle on Viper"

intent = bot._determine_intent(test_input)
print(f"Detected Intent: {intent}")

entities = bot._extract_entities(test_input)
print(f"Extracted Players: {entities['players']}")
print(f"Extracted Agents: {entities['agents']}")

if intent == "MATCH_PREDICTION":
    print("SUCCESS: Intent detected correctly.")
else:
    print("FAILURE: Intent not detected correctly.")
