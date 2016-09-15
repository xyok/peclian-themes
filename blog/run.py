from livereload import Server, shell
server = Server()
server.watch('content/*', shell('pelican content'))
server.watch('themes/think/*/*', shell('pelican content'))
server.watch('themes/think/static/*/*', shell('pelican content'))
# server.watch('./', shell('pelican content'))
server.serve(root='output')
