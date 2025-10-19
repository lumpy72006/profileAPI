# Create your views here.
import logging
import os
import requests
from datetime import datetime, timezone
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv("config.env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def me(request):
    logger.info("Processing /me request")
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Could not get cat fact.")
        logger.info("Fetched cat fact successfully")
    except Exception as e:
        logger.error(f"Failed to fetch cat fact: {e}")
        cat_fact = "Unable to get cat fact at the moment."
    data = {
        "status": "success",
        "user": {
            "email": os.getenv("USER_EMAIL", "hisoka@hunterXhunter"),
            "name": os.getenv("USER_NAME", "Hisoka Morow"),
            "stack": os.getenv("USER_STACK", "Bungee-Gum"),
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact,
    }
    logger.info("Constructed response data")

    return JsonResponse(data, content_type="application/json")
