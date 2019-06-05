from django import forms
from multiselectfield import MultiSelectFormField

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Feedback'
            }
        )

    )

class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'Placeholder':'Your Name'

            }
        )

    )
    email=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile No",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile No'
            }
        )
    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )
    courses = MultiSelectFormField(max_length=100, choices=COURSES_CHOICES)

    SHIFT_CHOICES = (
        ('mng', 'Morning'),
        ('aftn', 'Afternoon'),
        ('evng', 'Evining'),
        ('night', 'Night')

    )
    shifts = MultiSelectFormField(max_length=100, choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hydrabad'),

        ('bang', 'Banglore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    locations = MultiSelectFormField(max_length=200, choices=LOCATION_CHOICES)

    GENDER_CHOICES=(
        ('ml','Male'),
        ('f','Female')
    )
    gender = forms.CharField(
        widget=forms.RadioSelect(choices=GENDER_CHOICES)
    )

    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )