from supabase_init import supabase

def check_signatures():
    # Fetch signatures from the database
    signatures = supabase.table("signatures").select("*").execute()
    
    # Fetch logs from the database
    logs = supabase.table("login_attempts").select("*").execute()
    
    # Check for attack patterns
    for log in logs.data:
        for sig in signatures.data:
            if sig["pattern"] in log["user_agent"] or sig["pattern"] in log["username"]:
                # Log the alert
                supabase.table("alerts").insert({
                    "message": f"Attack detected: {sig['pattern']}",
                    "resolved": False
                }).execute()