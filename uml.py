# Let's create a UML diagram that represents the relationship between two databases ("Real Time Data" and "Stations Information") and an ETL pipeline and visualization function.

# I'll use the 'graphviz' library to generate the UML diagram.



from graphviz import Digraph



# Create a new directed graph

dot = Digraph(comment='ETL and Visualization UML')

# Add nodes for Databases and Components
dot.node('JC', 'JCDecaux API', shape="box")
dot.node('ETL', 'ETL Pipeline')
dot.node('RTD', 'Real Time Data (Database)', shape="box")
dot.node('SI', 'Stations Information (Database)', shape="box")
dot.node('Viz', 'Visualization Function')



# Add edges to represent relationships
dot.edge('ETL', 'RTD')
dot.edge('RTD', 'Viz')
dot.edge('SI', 'Viz')
dot.edge('JC', 'ETL')


# Render the diagram as a visual output

dot.render('uml_etl_viz', format='png', cleanup=True)

