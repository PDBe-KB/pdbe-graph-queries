"""PDB complex related queries
"""

Q_MAKE_PDB_COMPLEX = """
    MATCH (assembly:Assembly {PREFERED: 'True'})<-[rel:IS_PART_OF_ASSEMBLY]
    -(entity:Entity {TYPE:'p'})
    WITH assembly, rel, entity
    OPTIONAL MATCH (entity)-[:HAS_UNIPROT {BEST_MAPPING:'1'}]->(uniprot:UniProt)
    -[:HAS_TAXONOMY]->(tax:Taxonomy)
    OPTIONAL MATCH (entity)-[:HAS_RFAM]->(rfam:RfamFamily)
    WITH assembly.UNIQID AS assembly_id,
    CASE uniprot
        WHEN null
            THEN
                CASE rfam
                    WHEN null
                        THEN
                            CASE entity.POLYMER_TYPE
                                WHEN 'R'
                                    THEN 'RNA' +':UNMAPPED'
                                WHEN 'D'
                                    THEN 'DNA' +':UNMAPPED'
                                WHEN 'D/R'
                                    THEN 'DNA/RNA' +':UNMAPPED'
                                WHEN 'P'
                                    THEN 'NA_' +entity.UNIQID +'_' +rel.NUMBER_OF_CHAINS
                            END
                    ELSE
                        rfam.RFAM_ACC
                END
        ELSE uniprot.ACCESSION +'_' +rel.NUMBER_OF_CHAINS +'_' +tax.TAX_ID
    END AS accession ORDER BY accession
    WITH assembly_id AS assembly_id, COLLECT (DISTINCT accession) AS accessions
    WITH assembly_id AS assembly_id, REDUCE(s = HEAD(accessions),
    n in TAIL(accessions) | s +',' +n) AS accessions
    WITH accessions, COLLECT(DISTINCT assembly_id) AS assemblies
    WITH accessions AS accessions, REDUCE(s = HEAD(assemblies),
    n in TAIL(assemblies) | s +',' +n) AS assemblies
    RETURN accessions, assemblies
"""
"""
Cypher query to find unique assemblies and make unique complexes.

.. include:: rst_queries/Q_MAKE_PDB_COMPLEX.rst

:meta hide-value:
"""
