"""PDB entry related queries
"""

Q_ENTRY_KB_ANNOTATIONS = """
    MATCH
        (entry:Entry {ID:$entry_id})<-[:FUNPDBE_DATA_RELATED_TO]-
        (funpdb_entry:FunPDBeEntry)-[:HAS_EVIDENCE_CODE]->
        (evidence_code:EvidenceCodeOntology),
        (funpdb_entry)<-[:FUNPDBE_RESIDUE_GROUP_OF]-(funpdbe_group:FunPDBeResidueGroup)
    RETURN
        funpdb_entry.DATA_RESOURCE, funpdb_entry.RELEASE_DATE,
        funpdb_entry.RESOURCE_ENTRY_URL, COLLECT(DISTINCT evidence_code.ECO_CODE),
        COLLECT(DISTINCT funpdbe_group.LABEL)
"""
"""
Cypher query to retrieve PDBe-KB partner annotations for a PDB entry.

.. include:: rst_queries/Q_ENTRY_KB_ANNOTATIONS.rst

:meta hide-value:
"""
