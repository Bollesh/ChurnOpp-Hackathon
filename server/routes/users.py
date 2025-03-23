from fastapi import APIRouter, HTTPException, status
from db import supabase
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/users")
def get_users():
    try:
        response = supabase.table("users").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    

@router.get("/users/atrisk")
def get_at_risk_users():
    try:
        three_days_ago = datetime.now() - timedelta(days=3)
        interaction_response = supabase.table("interaction").select("user_id").lte("last_visit", three_days_ago.strftime('%Y-%m-%d')).execute()
        user_ids = [record["user_id"] for record in interaction_response.data]
        response = supabase.table("users").select("*").in_("user_id", user_ids).execute()
        return response.data
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )