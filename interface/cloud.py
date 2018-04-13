#!C:/Python27/python.exe
print 'Content-Type:text/html\n';

from neo4j import GraphDatabase
import urlparse, os;

try:
	id = int(urlparse.parse_qs(os.environ['QUERY_STRING'])['id'][0]);
	#print id;

	print '<!DOCTYPE html>';
	print "<html lang='en'>";
	print "<head>";
	print "<title>IMAGE CLOUD</title>";
	print '<style type="text/css">';
	print 'li.big';
	print '{';
	print 'font-size: 2em;';
	print '}';
	print 'li.small';
	print '{';
	print 'font-size: 1.2em;';
	print '}';
	print 'li.medium';
	print '{';
	print 'font-size:1.5em;';
	print '}';
	print '#img';
	print '{';
	print 'position:absolute;';
	print 'top:50px;';
	print 'left:50px;';
	print '}';
	print '#tags';
	print '{';
	print 'position:absolute;';
	print 'top:50px;';
	print 'left:50px;';
	print '}';
	print '</style>';
	print '<script type="text/javascript" src="http://localhost/tagcanvas.js"></script>';
			
	print '<script type="text/javascript">'	;
	print 'function init(){';
	print '//try';
	print '//{';
	print "TagCanvas.Start('cloud','tags',{textColour: 'maroon',outlineColour: '#ff00ff',reverse: true,depth: 0.8,maxSpeed: 0.05,weight: true,weightMode:'both',shape: 'sphere',weightGradient:{0:'coral',0.5:'blue', 1.0:'maroon'},noSelect: true,textHeight: 20,textFont: 'Comic Sans MS',hideTags: true,shadow: 'peachpuff',shadowOffset:[5,5],shadowBlur:1});";
	print '//}' ;
	print '//catch(e)'; 
	print '//{';
	print '// something went wrong, hide the canvas container';
	print "// document.getElementById('outer').style.display = 'none';";
	print '//}'
	print '}'
	print '</script>'
	print '</head>'
		
	print "<body onload='init()'>"
	print "<img src='http://localhost/img/1.jpg' width='50' id='img'></img>";
	db = GraphDatabase("D:\\preethi\\data\\graph");

	with db.transaction:
		author = db.node[id];
		relationships = author.relationships.outgoing;

		print '<div id="outer">';
		print '<canvas id="cloud" width="1300" height="600">';
		print '</canvas>';
		print '</div>';
		
		print "<div id='tags'>";
		print "<ul id='keywords' type='none'>";
		for rel in relationships:
			i = 0;
			if str(rel.type) == 'author_of':
				paper = rel.end;
				keywords = paper['key'];
				
				while i < len(keywords):
					if i == 0:
						print "<li class='big'><a>" + keywords[i] + "</a></li>";
					else:
						print "<li class='small'><a>" + keywords[i] + "</a></li>";
						
					i += 1;
					
	print '</ul>';
	print '</div>';
	#print '</img>';
	print '</body>';
	print '</html>';
except Exception as err:
	print err;
	