#!/usr/bin/env python3
"""
Demo script showing the hardcoded fallback emails.
This demonstrates what the email_getter function returns when API calls fail.
"""

import json
from datetime import datetime

def show_fallback_emails():
    """Show the hardcoded fallback emails that are returned when API calls fail."""
    
    # Hardcoded fallback emails (same as in email_getter.py)
    FALLBACK_EMAILS = [
        {
            "full_name": "Jashan Pratap Singh",
            "email": "jashanpratap123456@gmail.com",
            "company": "Tech Innovations Inc.",
            "job_title": "Senior Software Engineer",
            "location": "San Francisco, CA",
            "linkedin_url": "https://linkedin.com/in/jashanpratap-singh",
            "confidence": 0.95,
            "department": "Engineering",
            "extracted_at": datetime.now().isoformat(),
            "source": "fallback_hardcoded",
            "description": "Experienced full-stack developer with 8+ years in cloud architecture and machine learning. Specializes in Python, React, and AWS. Previously worked at Google and Microsoft."
        },
        {
            "full_name": "Harkit Singh Chhabra",
            "email": "harkitsinghchhabra@gmail.com",
            "company": "Digital Solutions Corp.",
            "job_title": "Product Manager",
            "location": "New York, NY",
            "linkedin_url": "https://linkedin.com/in/harkit-singh-chhabra",
            "confidence": 0.92,
            "department": "Product",
            "extracted_at": datetime.now().isoformat(),
            "source": "fallback_hardcoded",
            "description": "Strategic product leader with expertise in B2B SaaS and fintech. Led teams of 15+ engineers and designers. MBA from Stanford, previously at Stripe and PayPal."
        },
        {
            "full_name": "Jashan Pratap",
            "email": "jashanpratap123@gmail.com",
            "company": "AI Research Labs",
            "job_title": "Data Scientist",
            "location": "Seattle, WA",
            "linkedin_url": "https://linkedin.com/in/jashanpratap",
            "confidence": 0.88,
            "department": "Research & Development",
            "extracted_at": datetime.now().isoformat(),
            "source": "fallback_hardcoded",
            "description": "PhD in Computer Science from MIT. Expert in natural language processing and computer vision. Published 20+ papers in top-tier conferences. Previously at OpenAI and DeepMind."
        }
    ]
    
    print("=== Hardcoded Fallback Emails Demo ===")
    print("These emails are returned when API calls fail or no parameters are provided.\n")
    
    for i, email in enumerate(FALLBACK_EMAILS, 1):
        print(f"{i}. {email['full_name']}")
        print(f"   📧 Email: {email['email']}")
        print(f"   🏢 Company: {email['company']}")
        print(f"   💼 Job Title: {email['job_title']}")
        print(f"   📍 Location: {email['location']}")
        print(f"   🎯 Confidence: {email['confidence']}")
        print(f"   🏛️  Department: {email['department']}")
        print(f"   🔗 LinkedIn: {email['linkedin_url']}")
        print(f"   📝 Description: {email['description']}")
        print(f"   🏷️  Source: {email['source']}")
        print(f"   ⏰ Extracted: {email['extracted_at']}")
        print("-" * 80)
    
    print("\n=== JSON Output Format ===")
    print("When saved to a file, the output looks like this:")
    print(json.dumps(FALLBACK_EMAILS, indent=2))
    
    print("\n=== Usage Examples ===")
    print("The email_getter function will return these fallback emails when:")
    print("1. API search fails (no API key or network error)")
    print("2. No search parameters are provided")
    print("3. All search methods return empty results")
    print("\nExample calls that would trigger fallback emails:")
    print("- email_getter(company='Google')  # API fails")
    print("- email_getter(name='John Smith')  # API fails")
    print("- email_getter()  # No parameters")
    print("- email_getter(industry='Tech', country='USA')  # API fails")

def save_fallback_demo():
    """Save the fallback emails to a demo file."""
    FALLBACK_EMAILS = [
        {
            "full_name": "Jashan Pratap Singh",
            "email": "jashanpratap123456@gmail.com",
            "company": "Tech Innovations Inc.",
            "job_title": "Senior Software Engineer",
            "location": "San Francisco, CA",
            "linkedin_url": "https://linkedin.com/in/jashanpratap-singh",
            "confidence": 0.95,
            "department": "Engineering",
            "extracted_at": datetime.now().isoformat(),
            "source": "fallback_hardcoded",
            "description": "Experienced full-stack developer with 8+ years in cloud architecture and machine learning. Specializes in Python, React, and AWS. Previously worked at Google and Microsoft."
        },
        {
            "full_name": "Harkit Singh Chhabra",
            "email": "harkitsinghchhabra@gmail.com",
            "company": "Digital Solutions Corp.",
            "job_title": "Product Manager",
            "location": "New York, NY",
            "linkedin_url": "https://linkedin.com/in/harkit-singh-chhabra",
            "confidence": 0.92,
            "department": "Product",
            "extracted_at": datetime.now().isoformat(),
            "source": "fallback_hardcoded",
            "description": "Strategic product leader with expertise in B2B SaaS and fintech. Led teams of 15+ engineers and designers. MBA from Stanford, previously at Stripe and PayPal."
        },
        {
            "full_name": "Jashan Pratap",
            "email": "jashanpratap123@gmail.com",
            "company": "AI Research Labs",
            "job_title": "Data Scientist",
            "location": "Seattle, WA",
            "linkedin_url": "https://linkedin.com/in/jashanpratap",
            "confidence": 0.88,
            "department": "Research & Development",
            "extracted_at": datetime.now().isoformat(),
            "source": "fallback_hardcoded",
            "description": "PhD in Computer Science from MIT. Expert in natural language processing and computer vision. Published 20+ papers in top-tier conferences. Previously at OpenAI and DeepMind."
        }
    ]
    
    # Save to demo file
    with open("fallback_emails_demo.json", "w") as f:
        json.dump(FALLBACK_EMAILS, f, indent=2)
    
    print("✅ Saved fallback emails to 'fallback_emails_demo.json'")
    print("You can view this file to see the exact JSON format.")

if __name__ == "__main__":
    show_fallback_emails()
    print("\n")
    save_fallback_demo() 