email = input("Enter Your Email: ").strip()
name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print(f"Name: '{name}'\nDomain: '{domain_name}'")
