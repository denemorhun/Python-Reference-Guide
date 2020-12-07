# Getting more control over formatting
from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d %b %c"))