"""Small molecule related queries
"""

Q_COMPOUND_SIMILARITY = """
  MATCH
    (c:ChemicalComponent {ID:$het_code})-[s:HAS_SIMILARITY]-
    (other:ChemicalComponent {RELEASE_STATUS:"REL"})
  RETURN *
"""
"""
Cypher query to retrieve similar chemical components.

.. include:: rst_queries/Q_COMPOUND_SIMILARITY.rst

:meta hide-value:
"""
