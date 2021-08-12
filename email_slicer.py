email = input("Enter Your Email: ").strip()
name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print(f"Your user name is '{name}' and your domain is '{domain_name}'")
