import json
from dataclasses import dataclass, asdict


@dataclass
class AgentConfig:
    api_key : str
    api_secret : int
    model : str
    user_id : int

agentConfig = AgentConfig(
    api_key="ahsadh",
    api_secret= 12335,
    model= "gemini",
    user_id= 1
)

print(asdict(agentConfig))
print(type(agentConfig))

## Serialization and De-serialization
# Serialization > convert anything in python dictionary to json and vise a versa

#Creating a file

with open ("config.json", "r") as file:
    config_data = file.read()
    config_data = json.loads(config_data)

    print(config_data)
    print(config_data["model"])


