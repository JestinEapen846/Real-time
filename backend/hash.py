from supabase_init import supabase
import hashlib
from datetime import datetime

def hash_and_store(table_name, row_id, data):
    # Generate SHA-256 hash
    current_hash = hashlib.sha256(data.encode()).hexdigest()
    
    # Store the hash in Supabase
    supabase.table("data_hashes").insert({
        "table_name": table_name,
        "row_id": row_id,
        "hash": current_hash,
        "created_at": datetime.now().isoformat()
    }).execute()

# Example usage
hash_and_store("patients", "1", "John Doe,john@example.com,Diabetes")