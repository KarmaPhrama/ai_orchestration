#!/usr/bin/env python3
"""
Complete Email Workflow Script
Combines email extraction (email_getter) and email sending (email_sender).
This script demonstrates the complete workflow from extracting emails to sending them.
"""

import os
import json
import sys
from datetime import datetime

# Add current directory to path for imports
sys.path.append('.')

def run_complete_workflow():
    """Run the complete email workflow: extract emails and send them."""
    print("=== Complete Email Workflow ===")
    print("This script demonstrates the full workflow from email extraction to sending.\n")
    
    # Step 1: Extract emails
    print("Step 1: Extracting Email Addresses")
    print("=" * 50)
    
    try:
        from email_getter import email_getter
        
        # Example: Extract emails from text content
        sample_text = """
        Our team includes:
        - John Smith (john.smith@company.com)
        - Sarah Johnson (sarah.j@example.org)
        - Mike Wilson (mike.wilson@tech.com)
        Contact us at contact@company.com
        Support: support@company.com
        """
        
        print("Extracting emails from sample text...")
        extracted_emails = email_getter(
            text_content=sample_text,
            save_results=True,
            output_file="workflow_emails.json"
        )
        
        print(f"✅ Extracted {len(extracted_emails)} emails")
        for email in extracted_emails:
            print(f"  - {email.get('email', 'No email')}")
        
        # Step 2: Load email configuration
        print("\nStep 2: Email Configuration")
        print("=" * 50)
        
        config_file = "email_config.json"
        if not os.path.exists(config_file):
            print("❌ Email configuration not found.")
            print("Please run 'python3 email_config.py' to set up your email credentials.")
            return False
        
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        print("✅ Email configuration loaded")
        print(f"  - Sender: {config['sender_email']}")
        print(f"  - SMTP Server: {config['smtp_server']}")
        
        # Step 3: Send emails
        print("\nStep 3: Sending Emails")
        print("=" * 50)
        
        from email_sender import send_emails_from_extracted_data
        
        # Email template
        subject = "Professional Connection - Automated Outreach"
        body_template = """Hi {name},

I hope this email finds you well. I'm reaching out to connect professionally.

I came across your contact information and was impressed by your work. I believe we could have some interesting discussions about potential collaboration opportunities.

Would you be interested in a brief call or coffee chat to discuss potential synergies?

Best regards,
[Your Name]
[Your Company]
[Your Contact Information]

---
This email was sent as part of a professional networking outreach campaign."""
        
        # Confirm before sending
        print(f"Ready to send emails to {len(extracted_emails)} recipients.")
        confirm = input("Do you want to proceed with sending emails? (y/n): ").strip().lower()
        
        if confirm == 'y':
            results = send_emails_from_extracted_data(
                json_file="workflow_emails.json",
                sender_email=config["sender_email"],
                app_password=config["app_password"],
                subject=subject,
                body_template=body_template
            )
            
            print(f"\n📧 Email Sending Results:")
            print(f"  ✅ Successful: {results['success']}")
            print(f"  ❌ Failed: {results['failed']}")
            
            if results['errors']:
                print(f"  ⚠️  Errors: {results['errors']}")
            
            return True
        else:
            print("Email sending cancelled.")
            return False
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all required modules are installed.")
        return False
    except Exception as e:
        print(f"❌ Error in workflow: {e}")
        return False

def show_workflow_examples():
    """Show different workflow examples."""
    print("\n=== Workflow Examples ===")
    print("Here are different ways to use the email workflow:\n")
    
    examples = [
        {
            "name": "Text Parsing + Email Sending",
            "description": "Extract emails from text content and send professional emails",
            "code": """
# Extract emails from text
emails = email_getter(text_content="Contact us at test@example.com")
# Send emails
send_emails_from_extracted_data(
    json_file="extracted_emails.json",
    sender_email="your_email@gmail.com",
    app_password="your_app_password",
    subject="Professional Connection",
    body_template="Hi {name}, I hope this email finds you well..."
)"""
        },
        {
            "name": "API Search + Email Sending",
            "description": "Search for professionals using PDL API and send targeted emails",
            "code": """
# Search for professionals at a company
emails = email_getter(company="Google", size=10)
# Send personalized emails
send_emails_from_extracted_data(
    json_file="google_employees.json",
    sender_email="your_email@gmail.com",
    app_password="your_app_password",
    subject="Connecting with Google Professionals",
    body_template="Hi {name}, I'm reaching out regarding opportunities at {company}..."
)"""
        },
        {
            "name": "Industry Search + Email Sending",
            "description": "Find professionals in specific industries and send targeted outreach",
            "code": """
# Search for professionals in technology industry
emails = email_getter(industry="Technology", country="USA", size=20)
# Send industry-specific emails
send_emails_from_extracted_data(
    json_file="tech_professionals.json",
    sender_email="your_email@gmail.com",
    app_password="your_app_password",
    subject="Tech Industry Connection",
    body_template="Hi {name}, I'm reaching out to connect with fellow tech professionals..."
)"""
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example['name']}")
        print(f"   {example['description']}")
        print(f"   Code:")
        print(example['code'])
        print("-" * 80)

def show_best_practices():
    """Show best practices for email outreach."""
    print("\n=== Best Practices for Email Outreach ===")
    print("\n1. Personalization:")
    print("   - Use recipient names in emails")
    print("   - Reference their company and job title")
    print("   - Mention specific reasons for reaching out")
    
    print("\n2. Email Templates:")
    print("   - Keep emails concise and professional")
    print("   - Include a clear call-to-action")
    print("   - Provide your contact information")
    print("   - Use both plain text and HTML versions")
    
    print("\n3. Timing and Frequency:")
    print("   - Send emails during business hours")
    print("   - Don't send too many emails at once")
    print("   - Follow up appropriately")
    
    print("\n4. Compliance:")
    print("   - Include unsubscribe options")
    print("   - Respect CAN-SPAM regulations")
    print("   - Don't send to purchased lists")
    
    print("\n5. Testing:")
    print("   - Always test with your own email first")
    print("   - Check spam filters and deliverability")
    print("   - Monitor bounce rates and responses")

def main():
    """Main menu for the complete workflow."""
    while True:
        print("\n=== Complete Email Workflow Menu ===")
        print("1. Run complete workflow (extract + send)")
        print("2. Show workflow examples")
        print("3. Show best practices")
        print("4. Setup email configuration")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            run_complete_workflow()
        elif choice == "2":
            show_workflow_examples()
        elif choice == "3":
            show_best_practices()
        elif choice == "4":
            os.system("python3 email_config.py")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main() 