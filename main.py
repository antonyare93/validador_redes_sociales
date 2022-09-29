import time
import json
import instagram_scorer as ig_sc
import linkedin_scorer as lkn_sc

# Usuarios de prueba.
# El programa debe recibir un json con los valores relacionados en el json de prueba
with open('usuarios.json', 'r') as us:
    usuarios = json.load(us)


ig_privacy = False
ig_posts = 0
ig_followers = 0
ig_following = 0

rs = usuarios['usuarios']
for usuario in rs:
    if usuario == 'instagram':
        url = 'https://www.instagram.com/' + rs[usuario]

        ig_privacy, ig_posts, ig_followers, ig_following, ig_score, ig_status = ig_sc.get_values(url)
        
    elif usuario == 'twitter':
        url = 'https://twitter.com/' + rs[usuario]
    else:
        url = rs[usuario]
        if usuario == 'linkedin':
            lkn_followers, lkn_status = lkn_sc.existProfile(url)

time.sleep(300)