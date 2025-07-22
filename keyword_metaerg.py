import os
import pandas as pd
from pandas import ExcelWriter

os.chdir(r"/Users/ruchitasolanki/Downloads/RNA")
print('Reading tpm file...')
names = pd.read_csv("name_to_keyword_mapping.csv")

print('Making categories...')
keyword_categories = {
    "Cell_Envelope": [r"porin", r"D-alanine-D-alanine", r"Alanine racemase", r"Mur", r"Mra", r"Peptidoglycan"],
    "PS": [r"Photosystem", r"Bacteriorhodopsin", r"psb", r"psa", r"petA", r"petB", r"petC", r"petD", r"petE", r"petF", r"petH",
           r"puhA", r"pufA", r"pufB", r"pufC", r"pufM", r"pufL", r"chlorophyll", r"cytochrome b559"],
    "Citric_acid": [r"Pyruvate dehydrogenase", r"Pyruvate/2-oxoglutarate dehydrogenase", r'Citrate synthase',
                    r'Aconitase', r'Isocitrate dehydrogenase', r'2-Oxoglutarate dehydrogenas', r'Succinyl-CoA synthetase',
                    r'Succinate dehydrogenase', r'Fumarate hydratase', r'Malate', r'Isocitrate Lyase', r'Acetyl-CoA', r"NAD"],
    "Aminoacid_biosynthesis": [r"Alanine transaminase", r"aminotransferase", r'Asparagine', r'Glutamate', r'Glutamine',
                               r'Phosphoglycerate', r'Phosphoserine', r'Serine', r'Cysteine', r'Selenocysteine',
                               r'serine hydroxymethyltransferase', r'Threonine aldolase', r'Acetolactate', r'Ketol-acid',
                               r'Dihydroxyacid', r'transaminase', r'Isopropylmalate'],
    "Fatty_acid": [r"acyl-carrier-protein", r'C-acyltransferase', r'Fatty'],
    "Glycolysis": [r"Hexokinase", r"glucokinase", r'Glucose-6-phosphate-isomerase', r'Phosphofructokinase',
                   r'Fructose-bisphosphate', r'Triosephosphate isomerase', r'Glyceraldehyde-3-phosphate', r'Phosphoglycerate',
                   r'Phosphopyruvate', r'Pyruvate'],
    'Carbon_fixation': [r'rbcL', r"rbcS"],
    "Heme": [r"Heme", r"ferrochelatase", r'Polyprenyltransferase', r'Uroporphyrinogen-III methylase'],
    "Inositol_phosphate_biosynthesis": [r"Phosphoinositide phospholipase", r"Inositol", r'Triosephosphate', r'Fructose-1,6-bisphosphate',
                                       r'Phospholipase', r'phosphocholine'],
    "Iron_storage": [r"Bacterioferritin", r"Ferritin"],
    "Motility": [r"Flagellar", r"flagellin", r'pilin', r'Pilus', r'PilM'],
    #'Hydrogen_oxidation': [r'NiFe Hydrogenase', r"FeFe Hydrogenase", r'hox', r'ech Hydrogenase'],
    "Nitrogen_cycle": [r"Hydrazine", r"nitrate", r'Nitrite', r'Heme-copper', r'nitric', r'Nitrous',
                       r'Pmo', r'Smmo', r'hao', r'Nitrogenase', r'Urease', r'Urea', r'Cyanate lyase', r'Nitrile', r'nif', r'ure', r'urt', r'nap', r'octR', r'nrf'],
    "Respiration": [r"F0F1", r"Vacuolar", r'ATP synthase', r'NADH:ubiquinone', r'Cytochrome b6/f', r'Plastocyanin', r'Rieske Fe-S', 
                    r'quinol dependent', r'Heme/copper oxidase', r'Cyrochrome bd', r'Electron transport', r'Proton/sodium translocating pyrophosphatase', 
                    r"ndh", r"nuo", r"nqr", r"cytochrome c oxidase"],
    "Translation": [r"RNA polymerase", r"Ribosomal"],
    "Transport": [r"Twin arginine-target", r"translocase", r"Signal recognition", r"TolC", r"Periplasmic linker", r"HlyB",
                 r"Autotransported effector", r"secretion", r"Periplasmic", r"ExbB", r"TonB", r"ExbD", r'porter'],
    "Defense": [r"Defense", r"cas", r"CRISPR"],
    "Sulfur_cycle": [r"Adenylylsulfate", r"Sulfate", r"3-phosphoadenosine", r"phosphosulfate", r"Sulfite", r"Sulfur",
                     r"Thiosulfate", r"Sulfide", r"Thiosulfohydrolase", r"S-disulfanyl-L-cysteine", r"Thiosulfate",
                     r"Quinoprotein dehydrogenase", r'apr', r'dsr', r'sqr', r'fcc', r'sox'],
    "Secondary_metabolites": [r"isochorismate", r"antibiotic biosynthesis monooxygenase", r"cytochrome P450", r"shikimate"],
    "Other_elements": [r"Arsenite", r'Tetrachloroethene', r'PceA', r'Rdh', r'2-Haloacid', r"Decaheme", r'DMSO',
                       r'Selenate', r'chlorate', r'selenate'],
    "Toxin_antitoxin": [r"antitoxin" r"killer suppression"],
    "HP": [r"hypothetical"],
    "RNA_processing": [r"ribonuclease"],
    "tRNA": [r"tRNA"],
    "tmRNA": [r"transfer-messenger"],
    "Methylation": [r"SAM-dependent", r"50S ribosomal protein L11 methyltransferase", r"TrmD", r"16S rRNA (uracil(1498)-N(3))-methyltransferase", 
                    r"RNA methyltransferase", r"methyltransferase"],
    "Uknwn": [r"DUF", r"Uncharacterized"],
    "Phycocynin": [r"phycocyanin", r"phycobilisome", r"allophycocyanin"],
    "Carotenoids": [r"Orange"],
    "EPS": [r"PEP-CTERM"],
    "Stress_response": [r"DnaK", r"response regulator", r"CBS", r"GroES" r"GroEL", r"alcohol dehydrogenase", r"HtpG" r"ClpB" r"HslO", r"DnaJ",
                        r"CsbD", r"Crp/Fnr", r"CHASE2", r"GrpE", r"thioredoxin"r"Hsp70", r"GerMN", r"VOCs"],
    "ABC_transporters": [r"TIGR"],
    "Retrotransposon": [r"LTR retrotransposon"],
    "Transposase": [r"transposase"],
    "CCM": [r"CcmK", r"CcmL"],
    "Ribozyme Activity": [r"RNase P RNA component class A"],
    "Peptidoglycan Remodeling": [r"RlpA"],
    "Cell division": [r"septal", r"cell division protein", r"septum"]
}

print('Saving resluts...')
results = {}
for category, keywords in keyword_categories.items():
    pattern = '|'.join(keywords)
    results[category] = names[names['#Name'].str.contains(pattern, case=False, na=False)]

output_file = "name_categories.csv"
final_df.to_csv(output_file)
