

class EmailValidator:

	def __init__(self, min_length, mails, domains):
		self.min_length = min_length
		self.mails = mails
		self.domains = domains

	def __is_name_valid(self, name):
		return len(name) >= self.min_length

	def __is_mail_valid(self, mail):
		if "@" in mail and "." in mail:
			mail = mail[mail.index("@") + 1: mail.index(".")]
		return mail in self.mails

	def __is_domain_valid(self, domain):
		if "." in domain:
			domain = domain[domain.index(".") + 1:]
		return domain in self.domains

	def validate(self, email):
		data = email.split('@')
		username = data[0]
		mail, domain = data[1].split('.')

		return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)



# Test Code:
mails = ["me"]
domains = ["you", "he"]
email_validator = EmailValidator(5, mails, domains)
print(email_validator.validate("itsme@me.you"))
print(email_validator.validate("me@me.you"))
print(email_validator.validate("itsme@me.she"))
print(email_validator.validate("itsme@you.he"))

