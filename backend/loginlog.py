from supabase import create_client, Client
from datetime import datetime

url = "https://aagrglnhnzphclesxxmd.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhZ3JnbG5obnpwaGNsZXN4eG1kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAwNjg2NzIsImV4cCI6MjA1NTY0NDY3Mn0.yPEmAbpOXtt7IFuJgdk6Na1MTXJZP7IGxrOgigdtoXo"
supabase: Client = create_client(url, key)

def log_login_attempt(username, ip, status, user_agent):
    supabase.table("login_attempts").insert({
        "username": username,
        "ip": ip,
        "status": status,
        "user_agent": user_agent
    }).execute()

# Example usage
log_login_attempt("admin", "192.168.1.1", "FAILED", "Chrome/Windows")