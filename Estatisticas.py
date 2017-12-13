import json
import urllib.request
import datetime
from   Gameplay import *


def main_est(player_info):
    
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
        hero_total_wins.append((name, boneco['games'], boneco['win']))

    sort_heroes = sorted(hero_total_wins, key=lambda tup: tup[1], reverse=True)
    tax_wins = []
    loses = []

    
    for game in sort_heroes:
        loses.append(game[1]-game[2])
        tax_wins.append((game[2]/game[1]) * 100)

    
    main_game(player_info)
    
    statistics_page = """
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
              <a class="nav-link" href="Gameplay.html">Estilo de Jogo</a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" href="#">Estatísticas <span class="sr-only">(current)</span> </a>
            </li>
          </ul>

        </nav>

        <main role="main" class="col-sm-9 ml-sm-auto col-md-10 pt-3">
          <h1>Estatísticas</h1>

          <section class="row text-center placeholders">
            <div class="col-md-10 text-center">
              <img src=""" + player_info[2] + """  alt="A imagem não pode ser carregada" class="img-fluid rounded-circle" width="200" height="200">
              <h4>""" + player_info[0] + """</h4>
              <div class="text-muted">ID: """+ player_info[1] +"""</div>
            </div>
          </section>
          
          <h2>Herois Mais jogados</h2>
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Heroi</th>
                  <th>Quantidade de Partidas</th>
                  <th>Taxa de vitória</th>
                  <th>V/D</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>"""+  str(sort_heroes[0][0]) +"""</td>
                  <td>"""+  str(sort_heroes[0][1]) +"""</td>
                  <td>"""+      str(tax_wins[0])   +"""%</td>
                  <td>"""+  str(sort_heroes[0][2]) + """/""" + str(loses[0]) + """</td>
                </tr>
                <tr>
                  <td>"""+  str(sort_heroes[1][0]) +"""</td>
                  <td>"""+  str(sort_heroes[1][1]) +"""</td>
                  <td>"""+      str(tax_wins[1])   +"""%</td>
                  <td>"""+  str(sort_heroes[1][2]) + """/""" + str(loses[1]) + """</td>
                </tr>
                <tr>
                  <td>"""+  str(sort_heroes[2][0]) +"""</td>
                  <td>"""+  str(sort_heroes[2][1]) +"""</td>
                  <td>"""+      str(tax_wins[2])   +"""%</td>
                  <td>"""+  str(sort_heroes[2][2]) + """/""" + str(loses[2]) + """</td>
                </tr>				
                <tr>
                  <td>"""+  str(sort_heroes[3][0]) +"""</td>
                  <td>"""+  str(sort_heroes[3][1]) +"""</td>
                  <td>"""+      str(tax_wins[3])   +"""%</td>
                  <td>"""+  str(sort_heroes[3][2]) + """/""" + str(loses[3]) + """</td>
                </tr>
                <tr>
                  <td>"""+  str(sort_heroes[4][0]) +"""</td>
                  <td>"""+  str(sort_heroes[4][1]) +"""</td>
                  <td>"""+      str(tax_wins[4])   +"""%</td>
                  <td>"""+  str(sort_heroes[4][2]) + """/""" + str(loses[4]) + """</td>
                </tr>
                <tr>
                  <td>"""+  str(sort_heroes[5][0]) +"""</td>
                  <td>"""+  str(sort_heroes[5][1]) +"""</td>
                  <td>"""+      str(tax_wins[5])   +"""%</td>
                  <td>"""+  str(sort_heroes[5][2]) + """/""" + str(loses[5]) + """</td>
                </tr>
                <tr>
                  <td>"""+  str(sort_heroes[6][0]) +"""</td>
                  <td>"""+  str(sort_heroes[6][1]) +"""</td>
                  <td>"""+      str(tax_wins[6])   +"""%</td>
                  <td>"""+  str(sort_heroes[6][2]) + """/""" + str(loses[6]) + """</td>
                </tr>
                <tr>
                  <td>"""+  str(sort_heroes[7][0]) +"""</td>
                  <td>"""+  str(sort_heroes[7][1]) +"""</td>
                  <td>"""+      str(tax_wins[7])   +"""%</td>
                  <td>"""+  str(sort_heroes[7][2]) + """/""" + str(loses[7]) + """</td>
                </tr>	
                <tr>
                  <td>"""+  str(sort_heroes[8][0]) +"""</td>
                  <td>"""+  str(sort_heroes[8][1]) +"""</td>
                  <td>"""+      str(tax_wins[8])   +"""%</td>
                  <td>"""+  str(sort_heroes[8][2]) + """/""" + str(loses[8]) + """</td>
                </tr>	
                <tr>
                  <td>"""+  str(sort_heroes[9][0]) +"""</td>
                  <td>"""+  str(sort_heroes[9][1]) +"""</td>
                  <td>"""+      str(tax_wins[9])   +"""%</td>
                  <td>"""+  str(sort_heroes[9][2]) + """/""" + str(loses[9]) + """</td>
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
    
    file = open('Statistics.html', 'wb')
    file.write(statistics_page.encode('utf-8'))
    file.close()

