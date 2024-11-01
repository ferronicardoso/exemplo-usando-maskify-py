from maskify.masker import Masker

cpf = "123.456.789-01"
masked_cpf = Masker.mask_cpf(cpf, "*")
print("Masked CPF:", masked_cpf)  

# Output: "123.***.**9-01"

cnpj = "12.345.678/0001-99"
masked_cnpj = Masker.mask_cnpj(cnpj, "*")
print("Masked CNPJ:", masked_cnpj)  

# Output: "12.***.***/**01-99"

email = "usuario@exemplo.com"
masked_email = Masker.mask_email(email, "*")
print("Masked email:", masked_email)  

# Output: "u*****o@exemplo.com"

credit_card = "1234 1234 1234 1234"
masked_credit_card = Masker.mask_credit_card(credit_card, "*")
print("Masked credit card:", masked_credit_card)  

# Output: "**** **** **** 1234"

mobile_phone = "(11) 91234-5678"
masked_mobile_phone = Masker.mask_mobile_phone(mobile_phone)
print("Masked mobile phone:", masked_mobile_phone)  

# Output: "(11) *****-5678"

residential_phone = "(11) 1234-5678"
masked_residential_phone = Masker.mask_residential_phone(residential_phone)
print("Masked residential phone:", masked_residential_phone)  

# Output: "(11) ****-5678"

text = "Confidential"
masked_text = Masker.mask(text, start_position=2, length=8)
print("Masked custom:", masked_text)  

# Output: "Co********al"
