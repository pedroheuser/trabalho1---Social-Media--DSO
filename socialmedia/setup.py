import admin
import app
import usuario
import comment_manager

# Initialize the application
instancia = app.Aplicativo()

# cria um usuario admin
arthur = admin.Admin("arthur", "arthur@gmail.com", "1210")
instancia.add_admin(arthur)
arthur.login()

# cria uma instancia pra cuidar dos comentarios
comment_handler = comment_manager.CommentManager()

# cria um usuario e posta
pedro = usuario.Usuario("pedro", "teste", "teste")
daniel = usuario.Usuario("daniel", "teste", "teste")
post = arthur.postar("teste", "Tecnologia", instancia)

# User comments on the post
pedro.comentar(
    "esse post eh sobre economia",
    post=post,
    comment_manager=comment_handler,  # Pass the comment handler instance
)

daniel.curtir_post(post=post)
daniel.curtir_comentario(post.comentarios[0])


pedro.curtir_post(post=post)
instancia.printar_todos_posts()
print()
# Print comments on the post
print(post.comentarios[0].conteudo)
print(post.autor.username)
print(post.count_likes())
print(post.count_comentarios())
for i in post.comentarios:
    print(
        f"o comentario: '{i.conteudo}', do {i.autor.username}, possui {i.count_likes()} like(s). Quem curtiu foi o {i.likes[0].usuario.username}"
    )
    print(i.count_likes())
    print(i.autor.username)