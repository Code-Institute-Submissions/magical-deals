from django.contrib.auth.models import User
from django.db.models import Q


class CaseInsensitiveAuth:
    """Authenticate a User by using a case-insensitive query to check a
    combination of the supplied email/username and password."""

    def authenticate(self, username_or_email=None, password=None):
        """Get an instance of User using the supplied username
        or email (case insensitive) and verify the password."""
        # Filter all users by searching for a match by username/ email.
        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))
        if not users:
            return None

        # Then get the first result of the query (which is your user).
        user = users[0]
        # If the password is correct, return user object
        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        """Used by the Django authentication system to retrieve a
        User instance."""
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
