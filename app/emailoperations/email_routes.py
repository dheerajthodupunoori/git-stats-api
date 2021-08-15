from fastapi import APIRouter, Body, status
from starlette.responses import JSONResponse
from .email_message_model import Email
from .email_service import EmailService

email_operations_router = APIRouter(
    tags=["Email Operations"],
)


@email_operations_router.post("/sendEmail",
                              description="This API route is responsible to "
                                          "send an email to the application admin.",
                              status_code=status.HTTP_204_NO_CONTENT)
async def sendEmail(email: Email = Body(
    ...,
    examples={
        "example1": {
            "name": "Dheeraj Thodupunuri",
            "sender_email": "dheeraj.thodupunoori01@gmail.com",
            "email_subject": "Subject of email",
            "email_body": "Body of email"
        },
        "example2": {
            "name": "Dheeraj Thodupunuri",
            "sender_email": "dheeraj.thodupunoori01@gmail.com",
            "email_subject": "Subject of email",
            "email_body": "Body of email"
        },
        "example3": {
            "name": "Dheeraj Thodupunuri",
            "sender_email": "dheeraj.thodupunoori01@gmail.com",
            "email_subject": "Subject of email",
            "email_body": "Body of email"
        }
    }
)) -> JSONResponse:
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "drj.poc@gmail.com"
    pwd = "poc@0895"
    try:
        email_service = EmailService(email, smtp_server, port, sender_email, pwd)
        if email_service.sendEmail():
            return JSONResponse(status_code=200, content={"message": "email has been sent"})
        else:
            return JSONResponse(status_code=500, content={"message": "email has been sent"})
    except Exception as error:
        return JSONResponse(status_code=500, content={"message": error})
