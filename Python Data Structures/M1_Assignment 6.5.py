text = "X-DSPAM-Confidence:    0.8475   "

colon_position = text.find(":")
After_colon_Position = text[colon_position+1:]
print(float(After_colon_Position)) # No need of strip() function as float() function will automatically remove the leading and trailing whitespaces