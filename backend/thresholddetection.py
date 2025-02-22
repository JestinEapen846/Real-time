from supabase_init import supabase
from collections import defaultdict

failed_attempts = defaultdict(int)

def monitor_logs():
    # Fetch all login attempts from Supabase
    logs = supabase.table("login_attempts").select("*").execute()
    
    # Track failed attempts
    for log in logs.data:
        if log["status"] == "FAILED":
            key = (log["username"], log["ip"])
            failed_attempts[key] += 1
            
            # Trigger alert if threshold is breached
            if failed_attempts[key] > 5:
                supabase.table("alerts").insert({
                    "message": f"Brute-force detected: {log['username']} from {log['ip']}",
                    "resolved": False
                }).execute()

# Run the monitoring function
monitor_logs()