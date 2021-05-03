from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
    # subject = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
    # def send_email(self):
        # send email using the self.cleaned_data dictionary
        # pass
    #     if self.request.method == 'POST':
	# 	    form = ContactForm(self.request.POST)
    #         if form.is_valid():
    #             # subject = "Website Inquiry" 
    #             body = {
    #             'first_name': form.cleaned_data['first_name'], 
    #             'last_name': form.cleaned_data['last_name'], 
    #             'email': form.cleaned_data['email_address'], 
    #             'message':form.cleaned_data['message'], 
    #             }
    #             message = "\n".join(body.values())

    #             try:
    #                 send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
    #             except BadHeaderError:
    #                 return HttpResponse('Invalid header found.')
    #             return redirect ("home")
      
	# form = ContactForm()
	# return render(request, "main/contact.html", {'form':form})
