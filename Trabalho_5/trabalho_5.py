import json
import urllib.request

def main():
    
    url = urllib.request.urlopen('http://xkcd.com/info.0.json') 
    info = json.loads(url.read().decode())
    ultima = info['num']
    data_list = []
    nomes_list = []
    link_list = []

    numero_tirinhas = 6
    while numero_tirinhas > 0:
        url = urllib.request.urlopen('http://xkcd.com/'+ str(ultima) +'/info.0.json') 
        info = json.loads(url.read().decode())
        
        data = ''.join(str(info['day']) + '/' + str(info['month']) + '/' + str(info['year']) )
        
        data_list.append(data)
        nomes_list.append(str(info['safe_title']))
        link_list.append(str(info['img']))
        
        numero_tirinhas = numero_tirinhas - 1
        ultima = ultima - 1
             

    html = """
<!DOCTYPE html>
<html lang="en"><head>
    <title>XKCD</title>
    <!-- Bootstrap core CSS -->
    <link href="arquivos/bootstrap.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="arquivos/album.css" rel="stylesheet">
  </head>
  <body>
    <main role="main">
      <div class="album text-muted">
        <div class="container">
          <div class="row">
            <div class="card" align="center">
              <img data-src="holder.js/100px280?theme=thumb" src=""" + link_list[0] + """ data-holder-rendered="true">
              <p class="card-text">""" + data_list[0] + " --- " + nomes_list[0] + """</p>
            </div>
            <div class="card" align="center">
              <img data-src="holder.js/100px280?theme=thumb" src=""" + link_list[1] + """ data-holder-rendered="true">
              <p class="card-text">""" + data_list[1] + " --- " + nomes_list[1] + """</p>
            </div>
            <div class="card" align="center">
              <img data-src="holder.js/100px280?theme=thumb" src=""" + link_list[2] + """ data-holder-rendered="true">
              <p class="card-text">""" + data_list[2] + " --- " + nomes_list[2] + """</p>
            </div>
            <div class="card" align="center">
              <img data-src="holder.js/100px280?theme=thumb" src=""" + link_list[3] + """ data-holder-rendered="true">
              <p class="card-text">""" + data_list[3] + " --- " + nomes_list[3] + """</p>
            </div>
            <div class="card" align="center">
              <img data-src="holder.js/100px280?theme=thumb" src=""" + link_list[4] + """ data-holder-rendered="true">
              <p class="card-text">""" + data_list[4] + " --- " + nomes_list[4] + """</p>
            </div>
            <div class="card" align="center">
              <img data-src="holder.js/100px280?theme=thumb" src=""" + link_list[5] + """ data-holder-rendered="true">
              <p class="card-text">""" + data_list[5] + " --- " + nomes_list[5] + """</p>
            </div>
          </div>
        </div>
      </div>
    </main></body></html>
"""
    file = open('XKCD_Last6.html', 'wb')
    file.write(html.encode('utf-8'))
    file.close()
   
main()
