import pytz
from allauth.account.forms import SignupForm
from captcha.fields import CaptchaField
from django import forms
from django.db.models import Q
from mdeditor.fields import MDTextFormField

from website.models import (
    Bid,
    Hackathon,
    HackathonPrize,
    HackathonSponsor,
    IpReport,
    Issue,
    Job,
    Monitor,
    Organization,
    ReminderSettings,
    Repo,
    Room,
    UserProfile,
)


class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ["name", "description", "start_time", "end_time", "organization"]


class IssueForm(forms.ModelForm):
    captcha = CaptchaField()
    markdown_description = MDTextFormField(required=False)

    class Meta:
        model = Issue
        fields = [
            "url",
            "description",
            "domain",
            "label",
            "markdown_description",
            "cve_id",
        ]
        widgets = {
            "url": forms.URLInput(
                attrs={
                    "class": "w-full rounded-md border-gray-300 shadow-sm focus:border-[#e74c3c] focus:ring focus:ring-[#e74c3c] focus:ring-opacity-50 bg-white dark:bg-gray-900",
                    "placeholder": "https://github.com/owner/repo/issues/123",
                }
            ),
        }
