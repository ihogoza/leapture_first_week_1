import facebook as fb
access_token = 'EAAE8HPXMSLEBAALrRCfRLo8ZC6bJeN3yCfzyJb8ZAdo4lmDQmpwVWWUjKpIRrV1v13vkFnTYG8sZA6YxQvpohW5Glrr1efpYlUsfLMxCZC6yD7GA6DKy0zZByum2fNTGpOnmqu21nUDDbcW91FL7BeN46Dbl1tLlDhWRXLhGnCx6nIJESawuRZCQiwH5uWzjZA3f53SfS6lMFlbtUQxBpqd4otTFZCIA6jzPipjgMv3amsaCrtKQZBc5f'
asafb  = fb.GraphAPI(access_token)
# poster = asafb.put_object('me, 'posts', message = 'This is automated post!')
# print(poster)
post = asafb.get_object('3067954266780598_1985839204992115')
                 
print(post)

