# mainapp/forms.py
# # mainapp/forms.py
# from django import forms
# from .models import Department, Course
#
# class OrderForm(forms.Form):
#     name = forms.CharField(label='Name')
#     dob = forms.DateField(label='DOB', widget=forms.DateInput(attrs={'type': 'date'}))
#     age = forms.IntegerField(label='Age')
#     gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
#     phone_number = forms.CharField(label='Phone Number')
#     email = forms.EmailField(label='Email')
#     address = forms.CharField(label='Address')
#     department = forms.ModelChoiceField(label='Department', queryset=Department.objects.all())
#     course = forms.ModelChoiceField(label='Course', queryset=Course.objects.none())
#     purpose = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
#
#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)
#         self.fields['course'].queryset = Course.objects.none()
#         if 'department' in self.data:
#             try:
#                 department_id = int(self.data.get('department'))
#                 self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk:
#             self.fields['course'].queryset = self.instance.department.course_set

# mainapp/forms.py
from django import forms
from .models import Department, Course

class OrderForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB', widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone_number = forms.CharField(label='Phone Number')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address')
    department = forms.ModelChoiceField(label='Department', queryset=Department.objects.all())
    course = forms.ModelChoiceField(label='Course', queryset=Course.objects.all(), empty_label='Select a Course')
    purpose = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials_provide = forms.MultipleChoiceField(label='Materials Provide', choices=[('notebook', 'Debit Note Book'), ('pen', 'Pen'), ('exam_papers', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)
