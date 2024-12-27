import whitehat

p = whitehat.phonenumber(input("\nEnter the Phone_number with country code:"))
print("phone_number                            :",p.phone_number)
print("region                                  :",p.region)
print("timezone                                :",p.timezone)
print("provider                                :",p.provider)
print("carrier                                 :",p.carrier)
print("is_valid()                              :",p.is_valid())
print("phone_number.national_number.imag       :",p.phone_number.national_number.imag)
print("phone_number.national_number.real       :",p.phone_number.national_number.real)
print("phone_number.national_number.numerator  :",p.phone_number.national_number.numerator)
print("phone_number.national_number.denominator:",p.phone_number.national_number.denominator)
print("phone_number.country_code.real          :",p.phone_number.country_code.real)
print("phone_number.country_code.imag          :",p.phone_number.country_code.imag)
print("phone_number.country_code.denominator   :",p.phone_number.country_code.denominator)
print("phone_number.country_code.numerator     :",p.phone_number.country_code.numerator)
print("phone_number.extension                  :",p.phone_number.extension)
print("get_all_info(format=json)               :",p.get_all_info(format="json"))



