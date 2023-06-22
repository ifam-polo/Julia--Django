from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        conteudo = f'AEE email enviado'
        mail = EmailMessage(
            subject='Email enviado pelo django2',
            body=conteudo,
            from_email="contato@seudominio.com",
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()
