from supabase import create_client, Client

# Replace with your Supabase URL and API key
SUPABASE_URL = "https://aagrglnhnzphclesxxmd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhZ3JnbG5obnpwaGNsZXN4eG1kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAwNjg2NzIsImV4cCI6MjA1NTY0NDY3Mn0.yPEmAbpOXtt7IFuJgdk6Na1MTXJZP7IGxrOgigdtoXo"

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)