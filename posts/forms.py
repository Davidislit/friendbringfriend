from django import forms



class Candidate:
    person_candidate = forms.CharField(label='person_candidate',max_length=100)