from dotenv import load_dotenv
import os

from ocean import test_ocean

load_dotenv()

api_key = os.getenv("OCEAN_API_KEY")

test_ocean(api_key)