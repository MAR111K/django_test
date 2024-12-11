from django.core.mail import send_mail

def send_registration_email(user_email):
    subject = 'Welcome to My Site'
    message = 'Thank you for registering on our platform. Enjoy our services!'
    from_email = 'your_email@example.com'
    recipient_list = [user_email]
    print('OK')
    
    send_mail(subject, message, from_email, recipient_list)