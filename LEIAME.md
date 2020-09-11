# zoffline-helper

Scripts para configurar o Zwift (no Windows) para usar o zoffline, conectar ao Strava e baixar o perfil do Zwift.

## Para instalar o zwift-offline:

* Baixe o **zoffline_1.0.XXXXX.exe** de https://github.com/zoffline/zwift-offline/releases
* Baixe o **zoffline_helper.zip** de https://github.com/oldnapalm/zoffline-helper/releases
* Execute o script **configure_client**.
* Execute o **zoffline_1.0.XXXXX** e autorize quando o Firewall do Windows perguntar.
  * Uma pasta ``storage`` será criada para armazenar as suas informações.
* Mantenha a janela do zwift-offline aberta e abra o Zwift.
  * Se o "launcher" do Zwift já estava aberto (ícone do Zwift na área de notificação da barra de tarefas), feche-o e abra o Zwift novamente.

#### Ativando/Desativando o zwift-offline

Para usar o Zwift online normalmente, abra o atalho **Edit hosts** e remova a linha com os servidores do Zwift (ou adicione # no início da linha).

## Para carregar as atividades no Strava (opcional):

* Execute o **strava_auth** e autorize quando o Firewall do Windows perguntar.
* Abra http://localhost:8000/ no navegador, faça login no Strava e autorize o zwift-offline a carregar suas atividades.
* Será criado um arquivo **strava_token**, mova esse arquivo para a pasta ``storage\player_id``.

Somente atividades com **mais de 5 km** serão carregadas no Strava.

## Para baixar o seu perfil do Zwift (opcional):

* Execute o **get_profile**, digite seu login do Zwift (e-mail) e sua senha.
* Será criado um arquivo **profile.bin**, mova esse arquivo para a pasta ``storage`` (ele será movido para a pasta ``storage\player_id`` quando o zwift-offline for executado).

O zwift-offline **deve estar desativado** antes de rodar o get_profile.

## Para ativar o recurso de fantasmas (opcional):

* Crie um arquivo **enable_ghosts.txt** na pasta ``storage``.
* Quando salvar a atividade, um fantasma será gravado em ``storage\player_id\ghosts\<course>\<road>``.
* Se quiser que os fantasmas comecem na linha de largada, copie o arquivo [start_lines.csv](https://github.com/zoffline/zwift-offline/blob/master/start_lines.csv) para a pasta ``storage``.
  * Mova para cima as linhas de chegada de "Road to Sky" e "Ven-Top" para ativá-las.

## Nota:

Os executáveis são feitos com o pyinstaller. Um efeito colateral é que alguns antivírus detectam os executáveis do pyinstaller como malware. Esse é um problema conhecido e inevitável. Se preferir, você pode não usar estes executáveis e rodar diretamente do código fonte. Instruções em português em https://outlawcowboy.org/2019/04/26/zwift-offline/
