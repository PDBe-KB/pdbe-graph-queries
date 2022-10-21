"""UniProt related queries
"""

Q_UNIPROT_KB_ANNOTATION_PARTNERS = """
    MATCH
        (u:UniProt {ACCESSION:$uniprot_accession})-[:HAS_UNP_RESIDUE]->(ur:UNPResidue)
        <-[:MAP_TO_UNIPROT_RESIDUE]-(pdbRes:PDBResidue)<-[:FUNPDBE_ANNOTATION_FOR]-
        (resGroup:FunPDBeResidueGroup)-[:FUNPDBE_RESIDUE_GROUP_OF]->
        (funEntry:FunPDBeEntry)
    WHERE
        NOT funEntry.DATA_RESOURCE IN $excluded_partners
    RETURN
        COLLECT(DISTINCT funEntry.DATA_RESOURCE) AS partners
"""
"""
Cypher query to retrieve details of PDBe-KB partners for a UniProt accession.

.. include:: rst_queries/Q_UNIPROT_KB_ANNOTATION_PARTNERS.rst

:meta hide-value:
"""
