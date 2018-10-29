from datetime import datetime
import json
temp = datetime.utcnow()
print(temp)
dict = {}
ans = json.dumps(temp, indent=4, sort_keys=True, default=str)
print(ans)