# forms.py
from django import forms

class SetupTimeForm(forms.Form):
    def __init__(self, num_machines, job_names, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for m in range(1, num_machines + 1):
            for job_prev in job_names:
                for job_curr in job_names:
                    field_name = f"setup_{m}_{job_prev}_{job_curr}"
                    self.fields[field_name] = forms.IntegerField(
                        label=f"Setup Time M{m} {job_prev} → {job_curr}",
                        min_value=0,
                        initial=0,
                        required=True
                    )
