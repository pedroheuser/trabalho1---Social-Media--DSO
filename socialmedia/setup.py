import admin
import app
import usuario
import comment_manager
from interface_usuario import InteracaoUsuario


instancia = app.Aplicativo()

arthur = admin.Admin("arthur", "arthur@gmail.com", "1210121")
instancia.add_admin(arthur)


comment_handler = comment_manager.CommentManager()


pedro = instancia.add_usuario(usuario.Usuario("pedro", "teste@gmail.com", "testet"))
daniel = instancia.add_usuario(usuario.Usuario("daniel", "teste@gmail.com", "testetet"))
post = arthur.postar("Esse é um teste", "Tecnologia", instancia)


# User comments on the post
# pedro.comentar(
#     "esse post eh sobre economia",
#     post=post,
#     comment_manager=comment_handler,  # Pass the comment handler instance
# )

# daniel.curtir_post(post=post)
# daniel.curtir_comentario(post.comentarios[0])


# pedro.curtir_post(post=post)
# instancia.printar_todos_posts()
# print()
# # Print comments on the post
# print(post.comentarios[0].conteudo)
# print(post.autor.username)
# print(post.count_likes())
# print(post.count_comentarios())
# print(post.relatorio_likes())
# for i in post.comentarios:
#     print(
#         f"o comentario: '{i.conteudo}', do {i.autor.username}, possui {i.count_likes()} like(s). Quem curtiu foi o {i.likes[0].usuario.username}"
#     )
#     print(i.count_likes())
#     print(i.autor.username)


# Inicializando a interação com o usuário pedro
interacao_pedro = InteracaoUsuario(instancia)
interacao_pedro.login_tela()
