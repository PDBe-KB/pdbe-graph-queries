"""Small molecule related queries
  """

Q_COMPOUND_ATOM_DETAILS = """
MATCH (ligand:ChemicalComponent {ID:$chem_comp_id})-[:HAS_ATOM]->(atom:Atom)
RETURN atom.STEREO_CONFIG,
       atom.LEAVING_ATOM_FLAG,
       atom.ALT_ATOM_ID,
       atom.AROMATIC_FLAG,
       atom.ELEMENT_SYMBOL,
       atom.MODEL_CARTN_X_IDEAL,
       atom.MODEL_CARTN_Y_IDEAL,
       atom.MODEL_CARTN_Z_IDEAL,
       atom.CHARGE,
       atom.ID
"""
"""
Cypher query to retrieve wwPDB chemical component details along with
coordinates.

.. include:: rst_queries/Q_COMPOUND_ATOM_DETAILS.rst


Some other fancy description possibly with images goes here:

.. image:: /_static/imgs/filename.jpg
  :width: 200
  :alt: Alternative text

:meta hide-value:
"""
