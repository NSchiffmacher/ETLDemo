from graphviz import Digraph


dot = Digraph(comment='ETL and Visualization UML')

dot.node('JC', 'JCDecaux API', shape="box")
dot.node('ETL', 'ETL Pipeline')
dot.node('RTD', 'Real Time Data (Database)', shape="box")
dot.node('SI', 'Stations Information (Database)', shape="box")
dot.node('Viz', 'Visualization Function')

dot.edge('ETL', 'RTD')
dot.edge('RTD', 'Viz')
dot.edge('SI', 'Viz')
dot.edge('JC', 'ETL')

dot.render('uml_etl_viz', format='png', cleanup=True)

