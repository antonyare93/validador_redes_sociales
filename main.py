import time
import json
import instagram_scorer as ig_sc
import linkedin_scorer as lkn_sc
import twitter_scorer as tw_sc

# Usuarios de prueba.
# El programa debe recibir un json con los valores relacionados en el json de prueba
with open('usuarios.json', 'r') as us:
    usuarios = json.load(us)


ig_privacy = False
ig_posts = 0
ig_followers = 0
ig_following = 0
ig_status = True
lkn_followers = 0
lkn_status = True
tw_status = True


rs = usuarios['usuarios']
for usuario in rs:
    if usuario == 'instagram':
        url = 'https://www.instagram.com/' + rs[usuario]

        ig_privacy, ig_posts, ig_followers, ig_following, ig_score, ig_status = ig_sc.get_values(url)
        
    elif usuario == 'twitter':
        url = 'https://twitter.com/' + rs[usuario]
        tw_posts, tw_followers, tw_following, tw_score, tw_status = tw_sc.existProfile(url)
    else:
        url = rs[usuario]
        if usuario == 'linkedin':
            lkn_followers, lkn_status = lkn_sc.existProfile(url)

if ig_status and lkn_status:
    print("Crédito aprobado")
    print(f'Score IG: {ig_score} --- Resultado: {ig_status}')
    print(f'Seguidores Linkedin: {lkn_followers} --- Resultado: {lkn_status}')
    print(f'Score Tw: {tw_score} --- Resultado: {tw_status}')
else:
    print("Crédito rechazado")
    print(f'Score IG: {ig_score} --- Resultado: {ig_status}')
    print(f'Seguidores Linkedin: {lkn_followers} --- Resultado: {lkn_status}')
    print(f'Score Tw: {tw_score} --- Resultado: {tw_status}')