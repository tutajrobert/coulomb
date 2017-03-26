import static
import os

ws = static.Website('grot_site')

ws.style('main.css')

ws.title('GRoT> Graphical Resolver of T4s')

ws.header('Graphical Resolver of T4s',
          'View the project on GitHub: <a href="https://github.com/tutajrobert/grot"> tutajrobert/grot</a>&nbsp;&nbsp;&nbsp;//&nbsp;&nbsp;&nbsp;Correspond with the author: <a href="mailto:tutajrobert@gmail.com">tutajrobert</a>')

ws.menu([('main.html', 'Main'), 
         ('inst.html', 'Installation'), 
         ('manual.html', 'Manual'), 
         ('examples.html', 'Examples'), 
         ('tutorial.html', 'Tutorial'), 
         ('struct.html', 'Structure')])

ws.footer('Project is maintained by <a href="https://github.com/tutajrobert">tutajrobert</a>. Website style is strongly inspired by the <a href="http://flask.pocoo.org/">Flask webpage</a> and <a href="http://bettermotherfuckingwebsite.com/">better bloody website</a>. Content created using Coulomb electrostatic websites generator. Lavender workshop of creative spirit, Tri-Urbo, RNP!')

ws.page('main.html',
       open('grot_site' + os.sep + 'main.txt', 'r').read())

ws.publish()