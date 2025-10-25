from app.celery_worker import celery_app
import time

@celery_app.task
def send_email_task(to_email: str, subject: str, body: str):
    # Simulate sending email
    print(f"Sending email to {to_email} with subject {subject}")
    time.sleep(5)
    print("Email sent")
    return True
