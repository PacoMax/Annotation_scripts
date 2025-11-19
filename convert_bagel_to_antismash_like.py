from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import sys

def convert_bagel_gbk(input_gbk, output_gbk):
    records = list(SeqIO.parse(input_gbk, "genbank"))

    for record in records:
        # Aseguramos que tenga el campo 'molecule_type'
        record.annotations["molecule_type"] = "DNA"

        # Agrega campos necesarios al feature "source"
        for feature in record.features:
            if feature.type == "source":
                feature.qualifiers["cluster-number"] = ["1"]
                feature.qualifiers["product"] = ["RiPP"]

        # Añade aSDomain a genes candidatos
        for feature in record.features:
            if feature.type == "CDS":
                product = feature.qualifiers.get("product", [""])[0].lower()
                if "precursor" in product:
                    feature.qualifiers["aSDomain"] = ["PrePeptide"]
                elif "transport" in product:
                    feature.qualifiers["aSDomain"] = ["Transporter"]
                elif "modification" in product:
                    feature.qualifiers["aSDomain"] = ["Modifier"]

    # Escribe el nuevo archivo GenBank
    SeqIO.write(records, output_gbk, "genbank")
    print(f"✅ Archivo convertido guardado como: {output_gbk}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python convert_bagel_to_antismash_like.py <entrada.gbk> <salida.gbk>")
        sys.exit(1)
    input_gbk = sys.argv[1]
    output_gbk = sys.argv[2]
    convert_bagel_gbk(input_gbk, output_gbk)
