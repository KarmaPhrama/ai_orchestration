import os
import time
from peopledatalabs import PDLPY

def email_getter(industry: str, country: str, size: int = 30):
    """
    Search for people by industry and country, enrich profiles, and return list of dicts.
    All fields except name are optional; missing values will be None.
    """
    api_key = os.environ.get("PDL_API_KEY")
    if not api_key:
        raise RuntimeError("Set PDL_API_KEY in environment before using email_getter()")
    
    client = PDLPY(api_key=api_key)
    
    # Build Elasticsearch-style search query
    es_query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"job_industry": industry.lower()}},
                    {"term": {"location_country": country}}
                ]
            }
        }
    }
    
    search_resp = client.person.search(query=es_query, size=size)
    data = search_resp.json().get("data", [])
    
    results = []
    for person in data:
        enriched = client.person.enrichment(pdl_id=person.get("id")).json().get("data", {}) if person.get("id") else {}
        
        record = {
            "id": person.get("id"),
            "full_name": person.get("full_name"),
            "email": enriched.get("work_email") or enriched.get("email"),
            "phone": (enriched.get("phone_numbers") or [{}])[0].get("value"),
            "linkedin_url": enriched.get("linkedin_url"),
            "job_title": enriched.get("job_title"),
            "company": enriched.get("job_company_name"),
            "confidence": enriched.get("likelihood")
        }
        results.append(record)
        time.sleep(0.5)
    
    return results

# 🔍 Example usage:
if __name__ == "__main__":
    profiles = email_getter("Recruiting", "USA", size=20)
    for p in profiles:
        print(p)