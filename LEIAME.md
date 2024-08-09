# zoffline-helper

Scripts para configurar o Zwift (no Windows) para usar o zoffline, conectar ao Strava e baixar o perfil do Zwift.

## Para instalar o zwift-offline:

* Baixe o **zoffline_1.0.XXXXXX.exe** de https://github.com/zoffline/zwift-offline/releases/latest
* Baixe o **zoffline_helper.zip** de https://github.com/oldnapalm/zoffline-helper/releases/latest
* Execute o script **configure_client**.
* Execute o **zoffline_1.0.XXXXXX** e autorize quando o Firewall do Windows perguntar.
  * Uma pasta ``storage`` será criada para armazenar as suas informações.
* Mantenha a janela do zwift-offline aberta e abra o Zwift.
  * Se o "launcher" do Zwift já estava aberto (ícone do Zwift na área de notificação da barra de tarefas), feche-o e abra o Zwift novamente.

#### Ativando/Desativando o zwift-offline

Para usar o Zwift online normalmente, abra o atalho **hosts** e remova a linha com os servidores do Zwift (ou adicione # no início da linha).

## Para carregar as atividades no Strava (opcional):

* Obtenha o CLIENT_ID e CLIENT_SECRET de https://www.strava.com/settings/api
* Execute ``strava_auth.exe --client-id CLIENT_ID --client-secret CLIENT_SECRET`` e autorize quando o Firewall do Windows perguntar.
* Abra http://localhost:8000/ no navegador, faça login no Strava e autorize o zwift-offline a carregar suas atividades.
* Será criado um arquivo ``strava_token.txt``, mova esse arquivo para a pasta ``storage\1``.
* Se estiver testando, ande pelo menos 300 metros, atividades mais curtas não serão carregadas.

Entre no grupo **zoffline** no Strava https://www.strava.com/clubs/zoffline

## Para baixar o seu perfil do Zwift (opcional):

* Desative o zwift-offline (veja [Ativando/Desativando o zwift-offline](https://github.com/oldnapalm/zoffline-helper/blob/master/LEIAME.md#ativandodesativando-o-zwift-offline) acima).
* Execute o **get_profile**, digite seu login do Zwift (e-mail) e sua senha.
* Serão criados os arquivos ``profile.bin``, ``achievements.bin`` e ``economy_config.txt``, mova esses arquivos para a pasta ``storage\1``.
