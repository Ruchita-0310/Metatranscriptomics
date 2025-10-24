import os
import pandas as pd
from pandas import ExcelWriter

os.chdir(r"/Users/ruchitasolanki/Downloads/Cyano_paper/RNA_data_analysis")
print('Reading tpm file...')
names = pd.read_csv("name_to_keyword_mapping.csv")

print('Making categories...')
keyword_categories = {
    "Cell Envelope": [r"porin", r"D-alanine-D-alanine", r"Alanine racemase", r"Mur", r"Mra", r"Peptidoglycan", r"FtsX-like permease family protein"],
    "Photosystems": [r"Photosystem", r"Bacteriorhodopsin", r"psb", r"psa", r"petA", r"petB", r"petC", r"petD", r"petE", r"petF", r"petH", 
                     r"puhA", r"pufA", r"pufB", r"pufC", r"pufM", r"pufL", r"chlorophyll", r"cytochrome b559"],
    "Citric acid": [r"Pyruvate dehydrogenase", r"Pyruvate/2-oxoglutarate dehydrogenase", r'Citrate synthase',
                    r'Aconitase', r'Isocitrate dehydrogenase', r'2-Oxoglutarate dehydrogenas', r'Succinyl-CoA synthetase',
                    r'Succinate dehydrogenase', r'Fumarate hydratase', r'Malate', r'Isocitrate Lyase', r'Acetyl-CoA', r"NAD"],
    "Aminoacid biosynthesis": [r"Alanine transaminase", r"aminotransferase", r'Asparagine', r'Glutamate', r'Glutamine',
                               r'Phosphoglycerate', r'Phosphoserine', r'Serine', r'Cysteine', r'Selenocysteine',
                               r'serine hydroxymethyltransferase', r'Threonine aldolase', r'Acetolactate', r'Ketol-acid',
                               r'Dihydroxyacid', r'transaminase', r'Isopropylmalate'],
    "Fatty acid": [r"acyl-carrier-protein", r'C-acyltransferase', r'Fatty', r"beta-ketoacyl-ACP synthase"],
    "Glycolysis": [r"Hexokinase", r"glucokinase", r'Glucose-6-phosphate-isomerase', r'Phosphofructokinase',
                   r'Fructose-bisphosphate', r'Triosephosphate isomerase', r'Glyceraldehyde-3-phosphate', r'Phosphoglycerate',
                   r'Phosphopyruvate', r'Pyruvate'],
    'Carbon fixation': [r'rbcL', r"rbcS"],
    "Heme": [r"Heme", r"ferrochelatase", r'Polyprenyltransferase', r'Uroporphyrinogen-III methylase'],
    "Inositol_phosphate_biosynthesis": [r"Phosphoinositide phospholipase", r"Inositol", r'Triosephosphate', r'Fructose-1,6-bisphosphate',
                                       r'Phospholipase', r'phosphocholine'],
    "Iron storage": [r"Bacterioferritin", r"Ferritin"],
    "Motility": [r"Flagellar", r"flagellin", r'pilin', r'Pilus', r'PilM'],
    'Hydrogen oxidation': [r'NiFe Hydrogenase', r"FeFe Hydrogenase", r'hox', r'ech Hydrogenase'],
    "Nitrogen cycle": [r"Hydrazine", r"nitrate", r'Nitrite', r'Heme-copper', r'nitric', r'Nitrous',
                       r'Pmo', r'Smmo', r'hao', r'Nitrogenase', r'Urease', r'Urea', r'Cyanate lyase', r'Nitrile', r'nif', r'ure', r'urt', r'nap', r'octR', r'nrf'],
    "Respiration": [r"F0F1", r"Vacuolar", r'ATP synthase', r'NADH:ubiquinone', r'Cytochrome b6/f', r'Plastocyanin', r'Rieske Fe-S', 
                    r'quinol dependent', r'Heme/copper oxidase', r'Cyrochrome bd', r'Electron transport', r'Proton/sodium translocating pyrophosphatase', 
                    r"ndh", r"nuo", r"nqr", r"cytochrome c oxidase"],
    "Ribosomal Proteins": [r"Ribosomal protein"],
    "Transport": [r"Twin arginine-target", r"translocase", r"Signal recognition", r"TolC", r"Periplasmic linker", r"HlyB",
                 r"Autotransported effector", r"secretion", r"Periplasmic", r"ExbB", r"TonB", r"ExbD", r'porter'],
    "Defense": [r"Defense", r"cas", r"CRISPR", r"RAMP superfamily", r"viral"],
    "Sulfur cycle": [r"Adenylylsulfate", r"Sulfate", r"3-phosphoadenosine", r"phosphosulfate", r"Sulfite", r"Sulfur",
                     r"Thiosulfate", r"Sulfide", r"Thiosulfohydrolase", r"S-disulfanyl-L-cysteine", r"Thiosulfate",
                     r"Quinoprotein dehydrogenase", r'apr', r'dsr', r'sqr', r'fcc', r'sox'],
    "Other elements": [r"Arsenite", r'Tetrachloroethene', r'PceA', r'Rdh', r'2-Haloacid', r"Decaheme", r'DMSO',
                       r'Selenate', r'chlorate', r'selenate'],
    "Toxin antitoxin": [r"antitoxin", r"killer suppression", r"toxin-antitoxin", r"HigA family addiction module antitoxin"],
    "HP": [r"hypothetical"],
    "RNA processing": [r"ribonuclease"],
    "tRNA": [r"tRNA"],
    "tmRNA": [r"transfer-messenger"],
    "Methylation": [r"SAM-dependent", r"50S ribosomal protein L11 methyltransferase", r"TrmD", r"16S rRNA (uracil(1498)-N(3))-methyltransferase", 
                    r"RNA methyltransferase", r"methyltransferase", r"sulfotransferase"],
    "Uknown": [r"DUF", r"Uncharacterized"],
    "Phycocynin": [r"phycocyanin", r"phycobilisome", r"allophycocyanin"],
    "EPS": [r"PEP-CTERM"],
    "Stress response": [r"DnaK", r"response regulator", r"CBS", r"GroES", r"GroEL", r"alcohol dehydrogenase", r"HtpG", r"ClpB", r"HslO", r"DnaJ",
                        r"CsbD", r"Crp/Fnr", r"CHASE2", r"GrpE", r"thioredoxin", r"Hsp70", r"GerMN", r"VOCs", r"universal stress protein", 
                        r"mechanosensitive ion channel", r"STAS domain-containing protein", r"HEAT", r"co-chaperone GroES", r"MAG: chaperonin GroEL", 
                        r"metallophosphoesterase", r"putative addiction module antidote protein", r"SpoIIE", r"VOC", r"Ppx/GppA", r"HtpG", r"FtsH"],
    "Retrotransposon": [r"LTR retrotransposon"],
    "Transposase": [r"transposase"],
    "CCM": [r"CcmK", r"CcmL"],
    "Ribozyme Activity": [r"RNase P RNA component class A"],
    "Peptidoglycan Remodeling": [r"RlpA"],
    "Cell division": [r"septal", r"cell division protein", r"septum"],
    "rRNA": [r"23S ribosomal RNA", r"5S ribosomal RNA", r"16S ribosomal RNA"],
    "NRPS/PKS": [
        r"\bNRPS\b", r"\bPKS\b",
        r"amino acid adenylation domain", r"\bAdenylation\b|\bA\s*domain\b",
        r"\bcondensation\b|\bC\s*domain\b",
        r"\bPCP\b|\bpeptidyl carrier protein\b",
        r"thioesterase\b|\bTE\s*domain\b",
        r"\bACP\b|\bacyl carrier protein\b",
        r"\bKS\b|\bketosynthase\b",
        r"beta-?ketoacyl-?ACP", r"\bKR\b|\bketoreductase\b",
        r"\bDH\b|\bdehydratase\b", r"\bER\b|\benoylreductase\b",
        r"\bAT\b|\bacyltransferase\b", r"\bTE\b|\bthioesterase\b",
        r"\btrans-AT\b|\bstandalone acyltransferase\b",
        r"thioester reductase\b|\bR\s*domain\b",
        r"starter unit( acyltransferase)?",
        r"acyltransferases",
    ],
    "Terpenoids": [
        r"\bterpene\b|\bterpenoid\b", r"\bisoprenoid\b",
        r"GGPP|GGPPS|geranylgeranyl( diphosphate)? (synthase|reductase)",
        r"FPP|FPPS|farnesyl diphosphate synthase",
        r"\bidi\b|\bIPP isomerase\b|\bIsp[DFGH]\b|\bDXS\b|\bDXR\b|\bMEP\b|\bMVA pathway\b",
        r"phytoene (synthase|desaturase)|\bcrt(B|I|Y|E)\b|\bcarotenoid\b|\bcarotene\b",
        r"tocopherol cyclase", r"squalene|phytoene|hydroxysqualene",
        r"Red carotenoid-binding protein", r"\borange\b",
    ],
    "Siderophore": [
        r"\bsiderophore\b", r"SidA|IucD|PvdA", r"\bisochorismate\b|\bEntC\b|\bMenF\b",
        r"\benterobactin\b|\bEnt[A-F]\b|\bFep[ABCDG]\b",
        r"\bpvd[A-Z]\b|\bpch[A-Z]\b", r"\bybt[A-Z]\b|\byersiniabactin\b",
        r"\bNIS\b|\biuc[ABC]\b", r"TonB-?dependent receptor", r"\bFhu|Fec|Fep\b",
    ],
    "RiPPs and peptides": [
        r"\bRiPP\b|\bprecursor peptide\b|\bleader peptide\b",
        r"lanthipeptide|Lan(B|C|M|A|K)|class [I-V] lanthipeptide",
        r"lasso ?peptide|lasso cyclase|Lpt[BCE]",
        r"thiopeptide|Tcl|ThiF|YcaO|TfuA",  # YcaO/TfuA often in RiPPs
        r"sactipeptide|radical SAM|rSAM",
        r"linaridin|LinM|LinD",
        r"microviridin|Mdn",
        r"cyanobactin|Pat[A-E]|Tru[A-E]",
        r"LAP\b|linear azol(in|)e-?containing",
        r"bottromycin|Btm",
        r"glycocin|bacteriocin|\bTIGR\d+",
        r"RiPP precursor", r"TldD/PmbA", r"family peptidase",
    ],
    "Co-factors & Precursors": [
        r"\bshikimate\b|\bAro[ABCDEFG]\b|\bchorismate\b",
        r"3-?deoxy-7-?phosphoheptulonate|\bDAHP\b",
        r"\bprecorrin\b|\bcbi|cob[A-Z]\b|\bsirohydrochlorin chelatase\b",
        r"6,7-?dimethyl-8-?ribityllumazine synthase|\bRibE\b|\briboflavin\b",
        r"GTP cyclohydrolase I\b|\bFolE\b|\bQue[DEF]\b|\bpreQ0\b|\b7-?carboxy-7-?deazaguanine\b",
        r"\bcoenzyme F420\b|\bfbi[ABCDE]\b|\bcof[GH]\b|\bF\ *420\b|\bF420 hydrogenase\b",
        r"\bUbiD\b|\bUbiX\b|\bUbiA\b|\bdehydrogenase\b",
        r"\bHpsN\b",
    ],
    "Modifying enzymes": [
        r"\bcytochrome P450\b|\bCYP\d+", r"antibiotic biosynthesis monooxygenase",
        r"2OG-?Fe\(II\) oxygenase", r"\bSDR family oxidoreductase\b",
        r"\bFAD-?dependent (hydroxylase|monooxygenase)\b",
        r"glycosyltransferase( family)?", r"\bO-?methyltransferase\b|\bN-?methyltransferase\b|\bC-?methyltransferase\b",
        r"epimerase\b", r"halogenase|flavin-?dependent halogenase|prnA|rebH|thaL",
        r"Baeyer-?Villiger monooxygenase|BVMO",
        r"acyl-CoA ligase|AMP-?dependent synthetase",
    ],
    "Regulatory & Transport Genes": [
        r"\bTetR/AcrR\b|\bTetR\b", r"\bSARP\b", r"\bLAL regulator\b|\bLuxR-like\b|\bLuxR\b",
        r"\bMarR\b|\bMerR\b|\bLysR\b|\bAraC\b|\bXRE\b|\bsigma factor\b",
        r"diguanylate cyclase|GGDEF|EAL domain", r"ComF family protein",
        r"\bMFS transporter\b|\bABC transporter\b|\bRND efflux\b|\bMATE\b|\bSMR\b|\bpermease\b|\befflux pump\b",
        r"\bTonB-?dependent receptor\b",
        r"\bPhzF family phenazine\b",  # keeps your original cue
    ],
    "Resistance Genes": [
        r"macrolide 2'-?phosphotransferase",
        r"aminoglycoside (acetyltransferase|phosphotransferase|nucleotidyltransferase)",
        r"\bvan[HAXYZW]\b", r"\bble\b|\bbleomycin resistance\b",
        r"\bdrrA\b|\bdrrB\b|\bdrrAB\b",
        r"target protection|self-?resistance|antibiotic resistance protein"]
}

print('Saving resluts...')
results = {}
for category, keywords in keyword_categories.items():
    pattern = '|'.join(keywords)
    results[category] = names[names['#Name'].str.contains(pattern, case=False, na=False)]

# with ExcelWriter("name_categories.xlsx", engine='openpyxl') as writer:
#     for category, df in results.items():
#         if not df.empty:
#             df.to_excel(writer, sheet_name=category, index=False)
#         else:
#             print(f"{category} skipped.")

# print(f"Detailed data has been saved to name_categories.xlsx!")

# data = pd.DataFrame(columns=["Category"] + names.columns[1:].tolist())  
# for category, keywords in keyword_categories.items():
#     pattern = '|'.join(keywords)
#     filtered_df = names[names['#Name'].str.contains(pattern, case=False, na=False)]
#     row_data = {"Category": category}
#     for col in names.columns[1:]:  
#         row_data[col] = filtered_df[col].sum()

#     data = pd.concat([data, pd.DataFrame([row_data])], ignore_index=True)

# data.to_excel(f"keyword_category_sums.xlsx", index=False)
# print(f"Summaries has been saved to keyword_category_sums.xlsx")
    
# print(results)
# name_categories = pd.DataFrame.from_dict(results, orient="index")
# output_file = "name_categories.csv"
# name_categories.to_csv(output_file)

# Step 1: Create a list to hold the DataFrames with their category information
df_list = []

# Step 2: Iterate through the 'results' dictionary
for category_name, df_content in results.items():
    if not df_content.empty: # Only add if the DataFrame is not empty
        df_content['Category'] = category_name # Add the 'Category' column
        df_list.append(df_content)

# Step 3: Concatenate all DataFrames in the list
if df_list: # Check if the list is not empty before concatenating
    final_df = pd.concat(df_list, ignore_index=True)
else:
    final_df = pd.DataFrame() # Create an empty DataFrame if no results were found

# Display the resulting DataFrame
# print(final_df)
output_file = "name_categories_all.csv"
final_df.to_csv(output_file)
