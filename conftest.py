import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class EnvironmentVars:
    BaseURL = os.getenv("BASE_URL")
