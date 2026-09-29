from datetime import datetime
import random
now = datetime.now()
randnum = random.randint(1000, 9999)
date = now.strftime("%Y-%m-%d")

print(f"Contact ID: {randnum}, Added on: {date}")