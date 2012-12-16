from userena.models import UserenaSignup

class ActivationError(Exception):
    pass

def check_user_activation(activation_key):
    try:
        userena = UserenaSignup.objects.get(activation_key = activation_key)
    except:
        raise ActivationError()
    else:
        print userena

def activate_user(activation_key, password):
    user = UserenaSignup.objects.activate_user(activation_key)
    user.set_password(password)
    user.save()

    return user


