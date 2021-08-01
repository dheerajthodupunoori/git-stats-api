from pydantic import BaseModel, Field


class Email(BaseModel):
    name: str = Field(title="Name of the user",
                      description="Name of the user who want to send email to the application admin",
                      example="Dheeraj Thodupunuri")
    sender_email: str = Field(title="Email address of the user",
                              description="Email address of the user who want to send an email to the application "
                                          "admin.",
                              example="dheeraj.thodupunoori01@gmail.com")
    email_subject: str = Field(title="Email subject", example="Subject")
    email_body: str = Field(title="Email Body", example="Body")

    class Config:
        schema_extra = {
            "example": {
                "name": "Dheeraj Thodupunuri",
                "sender_email": "dheeraj.thodupunoori01@gmail.com",
                "email_subject": "Subject of email",
                "email_body": "Body of email"
            }
        }
