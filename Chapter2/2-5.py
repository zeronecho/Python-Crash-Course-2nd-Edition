
# 练习2-5 名言

# 打出引号的练习:如果想打出双引号就用单引号+双引号的组合

first_name="albert"
last_name="einstein"
full_name=f"{first_name} {last_name}"

sentence="A person who never made a mistake never tried anything new."


print(f'{full_name.title()} once said, "A person who never made a mistake never tried anything new."')
print(f'{full_name.title()} once said, "{sentence}"')

