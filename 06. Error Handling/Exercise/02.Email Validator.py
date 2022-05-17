

class NameTooShortError(Exception):
	pass


class MustContainAtSymbolError(Exception):
	pass


class InvalidDomainError(Exception):
	pass


def email_validator(email):
	while True:
		email_sub = email.find('@')
		if email_sub == -1:
			raise MustContainAtSymbolError("Email must contain @")

		email_name = email[:email.index('@')]
		email_name_len = len(email_name)
		if email_name_len <= 4:
			raise NameTooShortError("Name must be more than 4 characters")

		domains_list = [".com", ".bg", ".net", ".org"]
		email_domain = email[email.index('.'):]  # peter@gmail.com
		if email_domain not in domains_list:
			raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

		print("Email is valid")
		email = input()


email = input()
email_validator(email)