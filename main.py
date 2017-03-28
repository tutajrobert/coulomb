import static
import os

ws = static.Website('grot_site')

ws.style('main.css')

ws.title('GRoT> Graphical Resolver of T4s')

ws.header('GRAPHICAL RESOLVER of T4s',
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
	   
ws.page('inst.html',
       open('grot_site' + os.sep + 'inst.txt', 'r').read())
	   
ws.page('manual.html',
       open('grot_site' + os.sep + 'manual.txt', 'r').read())
	   
ws.page('examples.html',
       open('grot_site' + os.sep + 'examples.txt', 'r').read())
	   
ws.page('tutorial.html',
       open('grot_site' + os.sep + 'tutorial.txt', 'r').read())
	   
ws.page('struct.html',
       open('grot_site' + os.sep + 'struct.txt', 'r').read())

ws.publish()
