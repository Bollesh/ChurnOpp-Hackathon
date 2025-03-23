from fastapi import APIRouter, HTTPException, status
from db import supabase
from datetime import datetime, timedelta

router = APIRouter()


@router.get("/data/interactionscore")
def get_interaction_score():
    try:
        response = supabase.table("visit").select("date, avg_interaction_score").order("date", desc=True).limit(7).execute()
        return response.data
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    