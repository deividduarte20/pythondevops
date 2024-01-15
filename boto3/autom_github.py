import os
import fileinput
import git

def substituir_informacoes(arquivo, antiga_informacao, nova_informacao):
    with fileinput.FileInput(arquivo, inplace=True, backup='.bak') as arquivo_modificado:
        for linha in arquivo_modificado:
            print(linha.replace(antiga_informacao, nova_informacao), end='')

def clonar_ou_atualizar_repo(repo_url, repo_path):
    if os.path.exists(repo_path):
        # O diretório já existe, então vamos apenas atualizar o repositório
        repo = git.Repo(repo_path)
        origin = repo.remote(name='origin')
        origin.pull()
    else:
        # O diretório não existe, então vamos clonar o repositório
        git.Repo.clone_from(repo_url, repo_path)

def main():
    # Diretório home do usuário
    user_home = os.path.expanduser("~")

    # Caminho absoluto para o diretório de destino
    repo_path = os.path.join(user_home, 'rundeck')

    # Clonar ou atualizar o repositório do GitHub
    repo_url = 'git@github.com:deividduarte20/rundeck.git'
    clonar_ou_atualizar_repo(repo_url, repo_path)

    # Verificar se o diretório existe antes de inicializar o repositório
    if os.path.exists(repo_path):
        # Entrar no diretório do repositório
        os.chdir(repo_path)

        # Substituir informações nos arquivos desejados
        arquivo_alvo = 'teste.txt'
        antiga_informacao = 'SRE'
        nova_informacao = 'DevOps'
        substituir_informacoes(arquivo_alvo, antiga_informacao, nova_informacao)

        # Adicionar, commitar e fazer push das alterações
        repo = git.Repo(repo_path)
        repo.index.add([arquivo_alvo])
        repo.index.commit("Substituir {} por {}".format(antiga_informacao, nova_informacao))
        origin = repo.remote(name='origin')
        origin.push('main')
    else:
        print(f"O diretório {repo_path} não existe.")

if __name__ == "__main__":
    main()