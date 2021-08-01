from fastapi import APIRouter, Body, status
from .email_message_model import Email

# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from starlette.responses import JSONResponse

email_operations_router = APIRouter(
    tags=["Email Operations"],
)


# conf = ConnectionConfig(
#     MAIL_PASSWORD="poc@0895",
#     MAIL_FROM_NAME="Git stats",
#     MAIL_FROM="drj.poc@gmail.com",
#     MAIL_TLS=True,
#     MAIL_SSL=False,
#     USE_CREDENTIALS=True,
#     MAIL_USERNAME="Dheeraj",
#     MAIL_PORT=587,
#     MAIL_SERVER="smtp.gmail.com",
#     TEMPLATE_FOLDER=None
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
)):
    pass
    # message = MessageSchema(
    #     subject=email.email_subject,
    #     recipients="dheeraj.thodupunoori01@gmail.com",
    #     body=email.email_body + "from" + email.sender_email,
    # )
    # fm = FastMail(conf)
    # await fm.send_message(message)
    # return JSONResponse(status_code=200, content={"message": "email has been sent"})
