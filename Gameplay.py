import json
import urllib.request
import datetime

def main_game(player_info):
    
    url = urllib.request.urlopen('https://api.opendota.com/api/heroes')
    all_heroes = json.loads(url.read().decode())
    url.close()

    url = urllib.request.urlopen('https://api.opendota.com/api/players/'+ player_info[1] +'/heroes')
    most_played = json.loads(url.read().decode())
    url.close()

    hero_total_wins = [] 
    
    for top_10,boneco in enumerate(most_played):
        if(top_10 == 10):
            break
        hero_id = boneco['hero_id']
        for character in all_heroes:
            if int(character['id']) == int(hero_id):
                name = character['localized_name']
                break

        hero_total_wins.append((name, boneco['games'], (boneco['win']/boneco['games']) * 100 , int(hero_id)))

    sort_heroes = sorted(hero_total_wins, key=lambda tup: tup[1], reverse=True)
    sort_heroes = sorted(sort_heroes[:10], key=lambda tup: tup[2], reverse=True)
    sort_heroes = sort_heroes[0:3]

    lane = []
    role = []
    
    for hero in sort_heroes:
        url = urllib.request.urlopen('https://api.opendota.com/api/players/'+ player_info[1] +'/matches?hero_id='+ str(hero[-1]))
        ult_partidas = json.loads(url.read().decode())
        url.close()
        id_part = ult_partidas[0]["match_id"]

        url = urllib.request.urlopen('https://api.opendota.com/api/matches/'+ str(id_part))
        partidas = json.loads(url.read().decode())
        url.close()

        for player in partidas["players"]:
            if player["account_id"] == int(player_info[1]):
                if player["lane"] == 1:
                    caminho = "Bot"
                elif player["lane"] == 2:
                    caminho = "Mid"    
                elif player["lane"] == 3:
                    caminho = "Top"
                else:
                    caminho = "Indefinido"
                    
                if player["lane_role"] == 1:
                    position = "Lutador Principal"
                elif player["lane_role"] == 2:
                    position = "Lutador"
                elif player["lane_role"] == 3:
                    position = "Suporte"
                else:
                    position = "Indefinido"
                lane.append(caminho)
                role.append(position)
                break

    gameplay_page = """
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
              <a class="nav-link" href="Overview.html">Visão Geral</a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" href="Gameplay.html">Estilo de Jogo <span class="sr-only">(current)</span> </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="Statistics.html">Estatísticas</a>
            </li>
          </ul>

        </nav>

        <main role="main" class="col-sm-9 ml-sm-auto col-md-10 pt-3">
          <h1>Estilo de Jogo</h1>

          <section class="row text-center placeholders">
            <div class="col-md-10 text-center">
              <img src=""" + player_info[2] + """  alt="A imagem não pode ser carregada" class="img-fluid rounded-circle" width="200" height="200">
              <h4>""" + player_info[0] + """</h4>
              <div class="text-muted">ID: """+ player_info[1] +"""</div>
            </div>
          </section>
          
          <h2>Melhores Herois de Acordo com a Análise</h2>
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Heroi</th>
                  <th>Taxa de vitórias</th>
                  <th>Lane Principal</th>
                  <th>Função Principal</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>""" + str(sort_heroes[0][0]) + """</td>
                  <td>""" + str(sort_heroes[0][2]) + """%</td>
                  <td>""" +     str(lane[0])       + """</td>
                  <td>""" +     str(role[0])       + """</td>
                </tr>
                <tr>
                  <td>""" + str(sort_heroes[1][0]) + """</td>
                  <td>""" + str(sort_heroes[1][2]) + """%</td>
                  <td>""" +     str(lane[1])       + """</td>
                  <td>""" +     str(role[1])       + """</td>
                </tr>
                <tr>
                  <td>""" + str(sort_heroes[2][0]) + """</td>
                  <td>""" + str(sort_heroes[2][2]) + """%</td>
                  <td>""" +     str(lane[2])       + """</td>
                  <td>""" +     str(role[2])       + """</td>
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
    
    file = open('Gameplay.html', 'wb')
    file.write(gameplay_page.encode('utf-8'))
    file.close()



    
