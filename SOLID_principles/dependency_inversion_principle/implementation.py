from abc import ABC, abstractmethod

# Abstraction
class MessageService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

# Low-level module
class EmailService(MessageService):
    def send_message(self, message):
        print(f"Sending email: {message}")

# Another low-level module
class SMSService(MessageService):
    def send_message(self, message):
        print(f"Sending SMS: {message}")

# High-level module
class Notification:
    def __init__(self, service: MessageService):
        self.service = service  # Depends on abstraction

    def send(self, message):
        self.service.send_message(message)

# Testing
email_service = EmailService()
sms_service = SMSService()

notification_email = Notification(email_service)
notification_sms = Notification(sms_service)

notification_email.send("Hello via Email!")  # Output: Sending email: Hello via Email!
notification_sms.send("Hello via SMS!")      # Output: Sending SMS: Hello via SMS!