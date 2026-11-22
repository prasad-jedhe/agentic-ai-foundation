# 1. THE DATA BASELINE (Dictionaries & Lists)
# Simulating a database pull of user records. Dictionaries provide O(1) lookups.

users_database = [
    {"id": 101, "name": "Alice", "role": "admin", "is_active": True},
    {"id": 102, "name": "Bob", "role": "user", "is_active": False},
    {"id": 103, "name": "Charlie", "role": "editor", "is_active": True}
]


# Cleanly extract only the names of active users in a single line.
active_users = [user["name"] for user in users_database if user["is_active"]]
print(f"System Log: Found {len(active_users)} active users.\n")


# Dynamically build the context payload for the LLM.
context_block = ""
for index, name in enumerate(active_users, start=1):
    context_block += f"{index}. {name}\n"


# Utilizing multi-line triple quotes for clean prompt architecture
system_prompt = f"""
System Instruction: You are a corporate communication assistant.
Task: Write a highly professional welcome message for the following active team members.

Active Members:
{context_block}
Please keep the tone encouraging and brief.
"""

print("--- GENERATED PAYLOAD ---")
print(system_prompt)
print("-------------------------\n")

