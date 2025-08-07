from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def check_role(role):
    def _check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(_check)

@login_required
@check_role('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@check_role('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


