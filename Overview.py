import json
import sys
import urllib.request
import datetime
from Estatisticas import*

def main_init(p_id):

    url = urllib.request.urlopen('https://api.opendota.com/api/heroes')
    all_heroes = json.loads(url.read().decode())
    url.close()

    url = urllib.request.urlopen('https://api.opendota.com/api/players/'+ str(p_id) +'/matches?limit=5')
    all_jogos = json.loads(url.read().decode())
    url.close()

    ult_heroes = []
    ult_result = []
    ult_id     = []
    ult_time   = []
    ult_kda    = []

    for jogo in all_jogos:
        ult_heroes.append(jogo['hero_id'])
        for hero in all_heroes:
            if hero['id'] == ult_heroes[-1]:
                del ult_heroes[-1]
                ult_heroes.append(hero['localized_name'])
                break
        if (jogo['player_slot'] < 5 and jogo['radiant_win']  == True or jogo['player_slot'] > 5 and jogo['radiant_win'] == False):
            ult_result.append('Ganhou')
        else:
            ult_result.append('Perdeu')
            
        ult_id.append(str(jogo['match_id']))
        ult_time.append(str(datetime.timedelta(seconds=jogo['duration'])))
        ult_kda.append(str(jogo['kills'])+'/'+str(jogo['deaths'])+'/'+str(jogo['assists']))



    url = urllib.request.urlopen('https://api.opendota.com/api/players/'+str(p_id)) 
    info = json.loads(url.read().decode())    
    url.close()
    
    player_nick = info['profile']['personaname']
    player_id   = str(info['profile']['account_id'])
    player_avt  = info['profile']['avatarfull']

    list_player = [player_nick, player_id, player_avt]
    main_est(list_player)
    


    overview_page = """
<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <title>Player Analiser</title>
	
    <!-- Bootstrap core CSS -->
    <link href="Template_arquivos/bootstrap.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="Template_arquivos/dashboard.css" rel="stylesheet">
  </head>

  <body>
    <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="#">Player Analiser</a>
        <button class="navbar-toggler d-lg-none" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

      </nav>
    </header>

    <div class="container-fluid">
      <div class="row">
        <nav class="col-sm-3 col-md-2 d-none d-sm-block bg-light sidebar">
          <ul class="nav nav-pills flex-column">
            <li class="nav-item">
              <a class="nav-link active" href="#">Visão Geral <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="Gameplay.html">Estilo de Jogo</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="Statistics.html">Estatísticas</a>
            </li>
          </ul>


        </nav>

        <main role="main" class="col-sm-9 ml-sm-auto col-md-10 pt-3">
          <h1>Visão Geral</h1>

          <section class="row text-center placeholders">
            <div class="col-md-10 text-center">
              <img src=""" + player_avt + """  alt="A imagem não pode ser carregada" class="img-fluid rounded-circle" width="200" height="200">
              <h4>""" + player_nick + """</h4>
              <div class="text-muted">ID: """+ player_id +"""</div>
            </div>
          </section>

          <h2>Últimas Partidas</h2>
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Heroi</th>
                  <th>Resultado</th>
                  <th>ID da Partida</th>
                  <th>Duração</th>
                  <th>K/D/A</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>"""+ ult_heroes[0] +"""</td>
                  <td>"""+ ult_result[0] +"""</td>
                  <td>"""+ ult_id[0] +"""</td>
                  <td>"""+ ult_time[0] +"""</td>
                  <td>"""+ ult_kda[0] +"""</td>
                </tr>
                <tr>
                  <td>"""+ ult_heroes[1] +"""</td>
                  <td>"""+ ult_result[1] +"""</td>
                  <td>"""+ ult_id[1] +"""</td>
                  <td>"""+ ult_time[1] +"""</td>
                  <td>"""+ ult_kda[1] +"""</td>
                </tr>
                <tr>
                  <td>"""+ ult_heroes[2] +"""</td>
                  <td>"""+ ult_result[2] +"""</td>
                  <td>"""+ ult_id[2] +"""</td>
                  <td>"""+ ult_time[2] +"""</td>
                  <td>"""+ ult_kda[2] +"""</td>
                </tr>				
                <tr>
                  <td>"""+ ult_heroes[3] +"""</td>
                  <td>"""+ ult_result[3] +"""</td>
                  <td>"""+ ult_id[3] +"""</td>
                  <td>"""+ ult_time[3] +"""</td>
                  <td>"""+ ult_kda[3] +"""</td>
                </tr>
                <tr>
                  <td>"""+ ult_heroes[4] +"""</td>
                  <td>"""+ ult_result[4] +"""</td>
                  <td>"""+ ult_id[4] +"""</td>
                  <td>"""+ ult_time[4] +"""</td>
                  <td>"""+ ult_kda[4] +"""</td>
                </tr>				
	    </tbody>
            </table>
          </div>
        </main>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="Template_arquivos/jquery-3.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="Template_arquivos/popper.js"></script>
    <script src="Template_arquivos/bootstrap.js"></script>
 
</body></html>
"""
    
    file = open('Overview.html', 'wb')
    file.write(overview_page.encode('utf-8'))
    file.close()


