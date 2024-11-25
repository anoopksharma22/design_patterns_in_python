## Dependency Inversion Principle
High-level modules should not depend on low-level modules. \
Both should depend on abstractions.

In simpler terms:

- High-level modules (business logic) should not depend on the details of low-level modules (specific implementations).
- Instead, both should depend on abstractions (interfaces or abstract classes).
- This ensures flexibility and reduces tight coupling

### Example
```python
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self):
        self.email_service = EmailService()  # Direct dependency

    def send(self, message):
        self.email_service.send_email(message)

# Testing
notification = Notification()
notification.send("Hello, DIP!")  # Output: Sending email: Hello, DIP!
```

### Issue:
Here, a high-level class directly depends on a low-level implementation:
- The Notification class depends directly on EmailService, a concrete class.
- If we want to add an SMS service or change the email service, we need to modify the Notification class.

### Solution
We can fix this by introducing an abstraction (e.g., an interface) that both high-level and low-level modules depend on:

```python
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

```

### Explanation
#### Abstraction:

MessageService is an abstraction that both EmailService and SMSService implement.

#### Dependency Injection:

- The Notification class depends on MessageService, not a specific implementation.
- Specific services (like EmailService or SMSService) are passed as dependencies during instantiation.

#### Benefits:

- Adding new services (e.g., Push Notifications) doesn't require modifying the 
Notification class.
- The code is more flexible, testable, and follows the Dependency Inversion Principle.

This design ensures that high-level modules (Notification) and low-level modules (EmailService, SMSService) are loosely coupled and depend on a shared abstraction.