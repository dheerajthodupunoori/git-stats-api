from fastapi import APIRouter, Body, status
from .email_message_model import Email
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.responses import JSONResponse
import smtplib, ssl

email_operations_router = APIRouter(
    tags=["Email Operations"],
)


# conf = ConnectionConfig(
#     MAIL_USERNAME="drj.poc@gmail.com",
#     MAIL_PASSWORD="poc@0895",
#     MAIL_PORT=587,
#     MAIL_SERVER="smtp.gmail.com",
#     MAIL_TLS=True,
#     MAIL_SSL=False,
# )


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
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, pwd)
        message = email.name + "\n" + email.sender_email + "\n" + \
                  email.email_subject + "\n" + email.email_body
        server.sendmail(sender_email, "dheeraj.thodupunoori01@gmail.com", message)
        return JSONResponse(status_code=200, content={"message": "email has been sent"})
    except Exception as error:
        return JSONResponse(status_code=500, content={"message": error})
    finally:
        server.quit()
